from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Periodo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    mes = models.CharField(max_length=255)
    desdricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.desdricao


