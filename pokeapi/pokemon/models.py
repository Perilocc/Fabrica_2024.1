from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nome = models.CharField(verbose_name = "Nome do Pokemon", max_length=20)
    tipo = models.CharField(verbose_name = "Tipo do Pokemon", max_length=20, blank = True, null = True)
    passiva = models.CharField(verbose_name = "Passiva do Pokemon", max_length=100, blank = True, null = True)
    movimentos = models.CharField(verbose_name = "Movimentos do Pokemon", max_length=100, blank = True, null = True)