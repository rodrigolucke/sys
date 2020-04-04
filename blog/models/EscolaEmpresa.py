from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from blog.models.Empresa import Empresa
from blog.models.Escola import Escola



class EscolaEmpresa(models.Model):
    escola_codigo = models.ForeignKey(Escola, on_delete=models.PROTECT)
    empresa_codigo = models.ForeignKey(Empresa, on_delete=models.PROTECT)
