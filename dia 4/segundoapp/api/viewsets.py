from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .. models import ViaCepModel
from .serializers import CepSerializer
import requests

class ViaCepViewSet(ModelViewSet):
    queryset = ViaCepModel.objects.all()
    serializer_class = CepSerializer
    
    def create(self, request):
        cep = request.data.get("cep", "00000000")
        
        site = f"https://viacep.com.br/ws/{cep}/json/" #informações puxadas do site com requests.get
        requisicao = requests.get(site)
        json = requisicao.json()
        
        cep = json.get('cep', '')
        logradouro = json.get('logradouro', '')
        complemento = json.get('complemento', '')
        bairro = json.get('bairro', '')
        localidade = json.get('localidade', '')
        uf = json.get('uf', '')
        
        dados_recebidos = { #recebendo valor nas variáveis do banco
            "cep": cep,
            "logradouro": logradouro,
            "complemento": complemento,
            "bairro": bairro,
            "localidade": localidade,
            "uf": uf 
        }

        meuserializer = CepSerializer(data = dados_recebidos)
        
        if meuserializer.is_valid(): #Validação de existência no db
            
            cep_pesquisado = ViaCepModel.objects.filter(cep=cep)
            cep_pesquisado_existe = cep_pesquisado.exists()
            
            if cep_pesquisado_existe:
                return Response({"aviso":"seu cep já existe no banco"})
            
            meuserializer.save() #save no banco
            return Response(meuserializer.data)
        else:
            return Response({"Aviso":"Te vira"})