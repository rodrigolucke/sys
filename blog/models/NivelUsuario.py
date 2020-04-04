from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import GroupManager

# Create your models here.
from blog.models.Escola import Escola



class NivelUsuario(GroupManager):
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

