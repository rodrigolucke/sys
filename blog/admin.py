from django.contrib import admin

# Register your models here.
from blog.models import Escola
from blog.models import Aluno
from blog.models import Serie
from blog.models import NivelEnsino
from blog.models import Turno
from blog.models import Empresa
from blog.models import Trajeto
from blog.models import NivelUsuario

admin.site.register(Escola)
admin.site.register(Aluno)
admin.site.register(Serie)
admin.site.register(NivelEnsino)
admin.site.register(Turno)
admin.site.register(Empresa)
admin.site.register(Trajeto)
admin.site.register(NivelUsuario)


