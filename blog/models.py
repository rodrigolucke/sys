from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from blog.models import Escola
from blog.models import Aluno
from blog.models import Serie
from blog.models import NivelEnsino
from blog.models import Turno
from blog.models import Empresa
from blog.models import Trajeto
from blog.models import NivelUsuario

class Escola(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.nome

class Aluno(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    acompanhante = models.CharField(max_lenght=255)
    escola_codigo = models.ForeignKey(Escola, on_delete=models.PROTECT)
    serie_codigo = models.ForeignKey(Serie, on_delete=models.PROTECT)
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)
    turno_codigo = models.ForeignKey(Turno, on_delete=models.PROTECT)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.nome

class Serie(models.Model):
    codigo = models.IntegerField(primary_key=True)
    serie = models.CharField(max_length=255)
    nivel_ensino_cod = models.ForeignKey(NivelEnsino, on_delete=models.PROTECT)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.serie

class NivelEnsino(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.descricao

class Turno(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.descricao


class Empresa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.nome


class Trajeto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.nome


class NivelUsuario(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.nome


class AlunoTrajeto(models.Model):
    aluno_trajeto_codigo = models.IntegerField(primary_key=True)
    passagens = models.IntegerField()
    dt_mes = models.DateField()
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)

    def _str_(self):
        return self.passagens

class EscolaEmpresa(models.Model):
    escola_codigo = models.ForeignKey(Escola, on_delete=models.PROTECT)
    empresa_codigo = models.ForeignKey(Empresa, on_delete=models.PROTECT)


class UsuarioEscola(models.Model):
    usuarios_codigo = models.Foreignkey(User, on_delete=models.PROTECT)
    escola_codigo = models.Foreignkey(Escola, on_delete=models.PROTECT)


class EmpresaTrajeto(models.Model):
    empresa_codigo = models.Foreignkey(Empresa, on_delete=models.PROTECT)
    trajeto_codigo = models.Foreignkey(Trajeto, on_delete=models.PROTECT)