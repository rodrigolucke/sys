from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Empresa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


