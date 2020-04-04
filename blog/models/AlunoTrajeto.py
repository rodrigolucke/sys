from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from blog.models.Aluno import Aluno
from blog.models.Trajeto import Trajeto


class AlunoTrajeto(models.Model):
    aluno_codigo = models.IntegerField(Aluno, on_delete=models.PROTECT)
    passagens = models.IntegerField()
    dt_mes = models.DateField()
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)

    def __str__(self):
        return self.passagens
