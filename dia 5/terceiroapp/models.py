from django.db import models

# Create your models here.

class ViaCepModel(models.Model):
    cep = models.CharField(verbose_name="Cep do usuário", max_length=20)
    logradouro = models.CharField(verbose_name ="Logradouro do usuario", max_length=100, blank=True, null=True)
    complemento = models.CharField(verbose_name ="Complemento do usuario", max_length=100, blank=True, null=True)
    bairro = models.CharField(verbose_name ="Bairro do usuario", max_length=100, blank=True, null=True)
    localidade = models.CharField(verbose_name ="Localidade do usuario", max_length=100, blank=True, null=True)
    uf = models.CharField(verbose_name ="Estado do usuario", max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.cep