from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from blog.models.Empresa import Empresa
from blog.models.Periodo import Periodo
from blog.models.Aluno import Aluno



class AlunoPeriodoEscola(models.Model):
    aluno_codigo = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    empresa_codigo = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    periodo_codigo = models.ForeignKey(Periodo, on_delete=models.PROTECT)