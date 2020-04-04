from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from blog.models.Escola import Escola


class NivelEnsino(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao

