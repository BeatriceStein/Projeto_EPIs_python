from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True)  
    setor = models.CharField(max_length=80)
    idade = models.PositiveIntegerField(null=True, blank=True)
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    

    def __str__(self):
        return f"{self.nome} ({self.setor})"
