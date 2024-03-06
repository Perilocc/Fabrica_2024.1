from django.db import models

# Create your models here.

class PessoaBancoDeDados(models.Model):
    
    primeiro_nome = models.CharField(verbose_name = "Meu primeiro nome", max_length = 20)
    segundo_nome = models.CharField(verbose_name = "Meu segundo Nome", max_length = 25)
    idade = models.IntegerField(verbose_name="Minha idade", blank = True, null = True)
    
    def __str__(self) -> str:
        return f"{self.primeiro_nome} {self.segundo_nome}"