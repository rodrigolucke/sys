from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Escola(models.Model):
    nome = models.TextField()
    telefone = models.TextField()
    email = models.TextField();
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

