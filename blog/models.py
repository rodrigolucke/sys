from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.contrib.auth.models import GroupManager


class Empresa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Localidade(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Trajeto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    cod_saida = models.ForeignKey(Localidade, on_delete=models.PROTECT, related_name="localidade_cod_saida")
    cod_destino = models.ForeignKey(Localidade, on_delete=models.PROTECT, related_name="localidade_cod_destino")
    distancia = models.FloatField()
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cod_saida.nome + " - " + self.cod_destino.nome

class EmpresaTrajeto(models.Model):
    empresa_codigo = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)


class Escola(models.Model):
    codigo = models.IntegerField(primary_key=True, default=0)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class EscolaEmpresa(models.Model):
    escola_codigo = models.ForeignKey(Escola, on_delete=models.PROTECT)
    empresa_codigo = models.ForeignKey(Empresa, on_delete=models.PROTECT)


class NivelEnsino(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao

class Periodo(models.Model):
    codigo_mes = models.IntegerField(primary_key=True)
    desdricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.desdricao

class Serie(models.Model):
    codigo = models.IntegerField(primary_key=True, default=0)
    serie = models.CharField(max_length=255)
    nivel_ensino_cod = models.ForeignKey(NivelEnsino, on_delete=models.PROTECT)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.serie


class Turno(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao


class Aluno(models.Model):
    matricula = models.IntegerField(primary_key=True, default=0)
    nome = models.CharField(max_length=255)
    acompanhante = models.CharField(max_length=255)
    escola_codigo = models.ForeignKey(Escola, on_delete=models.PROTECT)
    serie_codigo = models.ForeignKey(Serie, on_delete=models.PROTECT)
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)
    turno_codigo = models.ForeignKey(Turno, on_delete=models.PROTECT)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class AlunoPeriodoEscola(models.Model):
    aluno_codigo = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    empresa_codigo = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    periodo_codigo = models.ForeignKey(Periodo, on_delete=models.PROTECT)

class AlunoTrajeto(models.Model):
    aluno_codigo = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    passagens = models.IntegerField()
    dt_mes = models.DateField()
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)

    def __str__(self):
        return self.passagens


class UsuarioEscola(models.Model):
    codigo_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    cod_escola = models.ForeignKey(Escola, on_delete=models.PROTECT)

    def __str__(self):
        return self.cod_escola.nome + " - "  + self.codigo_usuario.username
