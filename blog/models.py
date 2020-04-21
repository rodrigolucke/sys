from django.contrib.auth.models import User
from django.db import models
import datetime
# As model field:


class Empresa(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    '''def save(self, *args, **kwargs):
            self.criado_em = datetime.datetime.now().time()
            self.criado_por_id = get_username()
            super(Empresa, self).save(*args,**kwargs)'''

    def __str__(self):
        return self.nome




class Localidade(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    '''def save(self, *args, **kwargs):
        self.criado_em = datetime.datetime.now().time()
        super(Localidade, self).save(*args, **kwargs)'''

    def __str__(self):
        return self.nome


class Escola(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    '''def save(self, *args, **kwargs):
        self.criado_em = datetime.datetime.now().time()
        super(Escola, self).save(*args, **kwargs)'''

    def __str__(self):
        return self.nome


class EscolaEmpresa(models.Model):
    escola_codigo = models.ForeignKey(Escola, on_delete=models.PROTECT)
    empresa_codigo = models.ForeignKey(Empresa, on_delete=models.PROTECT)


class Trajeto(models.Model):
    codigo = models.AutoField(primary_key=True)
    cod_saida = models.ForeignKey(Localidade, on_delete=models.PROTECT, related_name="localidade_cod_saida")
    cod_destino = models.ForeignKey(Localidade, on_delete=models.PROTECT, related_name="localidade_cod_destino")
    distancia = models.FloatField()
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    '''def save(self, *args, **kwargs):
        self.criado_em = datetime.datetime.now().time()
        super(Trajeto, self).save(*args, **kwargs)'''

    def __str__(self):
        return self.cod_saida.nome + " - " + self.cod_destino.nome

class EmpresaTrajeto(models.Model):
    empresa_codigo = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)

class NivelEnsino(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    ''' def save(self, *args, **kwargs):
        self.criado_em = datetime.datetime.now().time()
        super(NivelEnsino, self).save(*args, **kwargs)'''

    def __str__(self):
        return self.descricao

class Periodo(models.Model):
    codigo_mes = models.AutoField(primary_key=True)
    desdricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    '''def save(self, *args, **kwargs):
        self.criado_em = datetime.datetime.now().time()
        super(Periodo, self).save(*args, **kwargs)'''

    def __str__(self):
        return self.desdricao

class Serie(models.Model):
    codigo = models.AutoField(primary_key=True)
    serie = models.CharField(max_length=255)
    nivel_ensino_cod = models.ForeignKey(NivelEnsino, on_delete=models.PROTECT)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.criado_em = datetime.datetime.now().time()
        super(Serie, self).save(*args, **kwargs)


    def __str__(self):
        return self.serie


class Turno(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    '''def save(self, *args, **kwargs):
        self.criado_em = datetime.datetime.now().time()
        super(Turno, self).save(*args, **kwargs)'''

    def __str__(self):
        return self.descricao


class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    acompanhante = models.CharField(max_length=255)
    escola_codigo = models.ForeignKey(Escola, on_delete=models.PROTECT)
    serie_codigo = models.ForeignKey(Serie, on_delete=models.PROTECT)
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)
    turno_codigo = models.ForeignKey(Turno, on_delete=models.PROTECT)
    #criado_por = CurrentUserField()
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    '''def save(self, *args, **kwargs):
        self.criado_em = datetime.datetime.now().time()
        super(Aluno, self).save(*args, **kwargs)'''

    def __str__(self):
        return self.nome

class AlunoPeriodoEscola(models.Model):
    aluno_codigo = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    empresa_codigo = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    periodo_codigo = models.ForeignKey(Periodo, on_delete=models.PROTECT)

class AlunoTrajeto(models.Model):
    aluno_codigo = models.ForeignKey(Aluno, on_delete=models.PROTECT, default=1)
    passagens = models.IntegerField()
    dt_mes = models.ForeignKey(Periodo, on_delete=models.PROTECT)
    trajeto_codigo = models.ForeignKey(Trajeto, on_delete=models.PROTECT)

    def __str__(self):
        return self.passagens


class UsuarioEscola(models.Model):
    codigo_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    cod_escola = models.ForeignKey(Escola, on_delete=models.PROTECT)

    def __str__(self):
        return self.cod_escola.nome + " - " + self.codigo_usuario.username
