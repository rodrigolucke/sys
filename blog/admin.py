from django.contrib import admin

# Register your models here.
from blog.models.Aluno import Aluno
from blog.models.Empresa import Empresa
from blog.models.Escola import Escola
from blog.models.Localidade import Localidade
from blog.models.NivelEnsino import NivelEnsino
from blog.models.NivelUsuario import NivelUsuario
from blog.models.Serie import Serie
from blog.models.Trajeto import Trajeto
from blog.models.Turno import Turno

admin.site.register(Escola)
admin.site.register(Aluno)
admin.site.register(Serie)
admin.site.register(NivelEnsino)
admin.site.register(Turno)
admin.site.register(Empresa)
admin.site.register(Localidade)
admin.site.register(Trajeto)
#admin.site.register(NivelUsuario)


