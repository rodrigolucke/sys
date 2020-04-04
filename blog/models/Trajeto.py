from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from blog.models.Localidade import Localidade


class Trajeto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    cod_saida = models.ForeignKey(Localidade, on_delete=models.PROTECT, related_name="localidade_cod_saida")
    cod_destino= models.ForeignKey(Localidade, on_delete=models.PROTECT, related_name="localidade_cod_destino")
    distancia = models.FloatField()
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cod_saida.nome + " - " + self.cod_destino.nome