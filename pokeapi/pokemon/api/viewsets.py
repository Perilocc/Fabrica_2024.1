from rest_framework.viewsets import ModelViewSet
from .serializers import PokemonSerializer
from rest_framework.response import Response
from ..models import Pokemon
import requests

class PokemonViewSet(ModelViewSet):
    queryset =  Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    def create(self, request):
        nome = request.data.get("nome", "")
        site = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}/"
        
        try:
            requisicao = requests.get(site)
            json = requisicao.json()
            
            nome = json.get('name', '')
            tipo = [tipo["type"]["name"] for tipo in json.get("types", [])]
            passiva = [passiva["ability"]["name"] for passiva in json.get("abilities", [])]
            movimentos = [movimento["move"]["name"] for movimento in json.get("moves", [])[:4]]

            dados_recebidos = {
                "nome": nome,
                "tipo": ", ".join(tipo),
                "passiva": ", ".join(passiva),
                "movimentos": ", ".join(movimentos)
            }
            
            meuserializador = PokemonSerializer(data=dados_recebidos)
            
            if meuserializador.is_valid():
                pokemon_no_banco = Pokemon.objects.filter(nome=nome)
                pokemon_existe = pokemon_no_banco.exists()
                if pokemon_existe:
                    return Response({"aviso": "Esse Pokemon já existe no banco"})
                
                meuserializador.save()
                return Response(meuserializador.data)

            else:
                return Response({"aviso": "Esse Pokemon não existe ou é inválido"})
            
        except requests.exceptions.RequestException:
            return Response({"aviso": "O Pokémon fornecido é inválido ou não existe"})

    def delete(self, pk=None):
        try:
            pokemon = Pokemon.objects.get(id=pk)
            pokemon.delete()
            return Response({"aviso": "O Pokémon foi excluído com sucesso"})
            
        except Pokemon.DoesNotExist:
            return Response({"aviso": "Este Pokémon não existe"}) 