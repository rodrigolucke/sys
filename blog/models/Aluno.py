from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from blog.models.Escola import Escola
from blog.models.Serie import Serie
from blog.models.Trajeto import Trajeto
from blog.models.Turno import Turno


class Aluno(models.Model):
    matricula = models.IntegerField(primary_key=True, default=0)
    nome = models.CharField(max_length=255)
    acompanhante =  models.CharField(max_length=255)
    escola_codigo = models.ForeignKey(Escola, on_delete=models.PROTECT)
    serie_codigo = models.ForeignKey(Serie, on_delete=models.PROTECT)
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)
    turno_codigo = models.ForeignKey(Turno, on_delete=models.PROTECT)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
