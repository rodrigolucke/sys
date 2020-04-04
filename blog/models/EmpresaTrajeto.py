from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from blog.models.Empresa import Empresa
from blog.models.Trajeto import Trajeto


class EmpresaTrajeto(models.Model):
    empresa_codigo = models.Foreignkey(Empresa, on_delete=models.PROTECT)
    trajeto_codigo = models.Foreignkey(Trajeto, on_delete=models.PROTECT)