from django.db import models
from django.contrib.auth.models import User

# Create your models here
from blog.models.Escola import Escola
from blog.models.NivelUsuario import NivelUsuario

class UsuarioEscola(models.Model):
    usuario_codigo = models.Foreignkey(User, on_delete=models.PROTECT)
    escola_codigo = models.Foreignkey(Escola, on_delete=models.PROTECT)
    nivel_usuario = models.Foreignkey(NivelUsuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.usuario_codigo.nome + " - " + self.escola_codigo.nome
