from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import ViaCepModel
import requests
from django.http import HttpResponseRedirect
# Create your views here.

class ReceberCepView(CreateView):
    template_name = 'inserir_cep.html'
    success_url = '/lista'
    model = ViaCepModel
    fields=['cep']
    
    def form_valid(self, form):
        cep = form.cleaned_data.get('cep', '00000000')
        
        site = f"https://viacep.com.br/{cep}/json/"
        requisicao = requests.get(site)
        dados = requisicao.json()
        
        dados_cep = {
            'logradouro':   dados.get('logradouro', ''),
            'complemento':  dados.get('complemento', ''),
            'bairro':   dados.get('bairro', ''),
            'localidade':   dados.get('localidade', ''),
            'uf':   dados.get('uf', '')
        }
        
        banco_de_dados = ViaCepModel.objects.update_or_create(cep=cep, default=dados)
        
        return HttpResponseRedirect(self.success_url)
    
    class ListaCep(ListView):
        model = ViaCepModel
        template_name = "exibir_cep.html"
        context_object_name = "cep"
        
    class DetailCep(DetailView):
        model = ViaCepModel
        template_name = "detalhe_cep.html"
        