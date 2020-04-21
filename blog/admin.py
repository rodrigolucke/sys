from django.contrib import admin


# Register your models here.
#from blog.models.Aluno import Aluno
from .models import Aluno, AlunoTrajeto
#from blog.models.Empresa import Empresa
from .models import Empresa
#from blog.models.Escola import Escola
from .models import Escola
#from blog.models.Localidade import Localidade
from .models import Localidade
#from blog.models.NivelEnsino import NivelEnsino
from .models import NivelEnsino
#from blog.models.NivelUsuario import NivelUsuario
from .models import Periodo
#from blog.models.Periodo import Periodo
#from blog.models.Serie import Serie
from .models import Serie
#from blog.models.Trajeto import Trajeto
from .models import Trajeto
#from blog.models.Turno import Turno
from .models import Turno
from .models import UsuarioEscola
from .models import AlunoTrajeto

#admin.site.register(Escola)
@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):

    fields = ['nome', 'telefone']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)

#admin.site.register(Aluno)
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    fields = ['nome', 'acompanhante', 'escola_codigo', 'trajeto_codigo', 'turno_codigo', 'serie_codigo']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)

#admin.site.register(Serie)
@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):

    fields = ['serie', 'nivel_ensino_cod']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)

#admin.site.register(NivelEnsino)
@admin.register(NivelEnsino)
class NivelEnsinoAdmin(admin.ModelAdmin):

    fields = ['descricao']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)


#admin.site.register(Turno)
@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):

    fields = ['descricao']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)

#admin.site.register(Empresa)
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):

    fields = ['nome', 'telefone']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)

#admin.site.register(Localidade)
@admin.register(Localidade)
class LocalidadeAdmin(admin.ModelAdmin):

    fields = ['nome']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)

#admin.site.register(Trajeto)
@admin.register(Trajeto)
class Trajetodmin(admin.ModelAdmin):

    fields = ['cod_saida', 'cod_destino', 'distancia', 'cod_empresa']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):

    fields = ['desdricao']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)


#admin.site.register(UsuarioEscola)
@admin.register(UsuarioEscola)
class UsuarioEscolaAdmin(admin.ModelAdmin):

    fields = ['codigo_usuario', 'cod_escola']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)

#admin.site.register(AlunoTrajeto)
@admin.register(AlunoTrajeto)
class UsuarioEscolaAdmin(admin.ModelAdmin):

    fields = ['aluno_codigo', 'passagens','dt_mes', 'trajeto_codigo']

    def save_model(self, request, obj, form, change):
            obj.criado_por_id = request.user.id
            super().save_model(request, obj, form, change)
