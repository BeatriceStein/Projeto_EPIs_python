from django.db import models
from django.utils import timezone

class EPI(models.Model):
    CATEGORIAS = [
        ('proteção da cabeça', 'Proteção da Cabeça'),
        ('proteção auditiva','Proteção Auditiva'),
        ('proteção ocular e facial', 'Proteção Ocular e Facial'),
        ('proteção mãos e braços', 'Proteção mãos e braços'),
        ('boproteção pernas e pés', 'Proteção pernas e pés'),
        ('proteção respiratória', 'Proteção Respiratória'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do EPI")
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='outro')
    quantidade = models.PositiveIntegerField(default=0)
    validade = models.DateField(verbose_name="Validade do EPI", default=timezone.now)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.categoria})"

    class Meta:
        verbose_name = "EPI"
        verbose_name_plural = "EPIs"
        ordering = ['nome']
