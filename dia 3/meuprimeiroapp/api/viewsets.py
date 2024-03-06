from rest_framework.viewsets import ModelViewSet
from .serializers import PessoaSerializer
from ..models import PessoaBancoDeDados

class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = PessoaBancoDeDados.objects.all() # puxa todas as pessoas do models