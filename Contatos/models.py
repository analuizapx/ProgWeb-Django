from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField


# Create your models here.

class Psicologo(models.Model):
    nome =models.CharField(max_length=100);
    idade = models.IntegerField()
    local = models.CharField(max_length=100,verbose_name="Localização do consultório");
    atendeOnline = models.BooleanField();
    abordagem = models.CharField(max_length=100,verbose_name="Linha que você trabalha:");
    curriculum = models.CharField(max_length=300,verbose_name="Lattes:");

    def __str__(self):
        return self.nome + ': ' + self.email




