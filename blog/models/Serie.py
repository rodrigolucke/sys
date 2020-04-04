from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from blog.models.Escola import Escola
from blog.models.NivelEnsino import NivelEnsino


class Serie(models.Model):
    codigo = models.IntegerField(primary_key=True, default=0)
    serie = models.CharField(max_length=255)
    nivel_ensino_cod = models.ForeignKey(NivelEnsino, on_delete=models.PROTECT)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.serie
