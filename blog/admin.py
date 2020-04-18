from django.contrib import admin


# Register your models here.
#from blog.models.Aluno import Aluno
from .models import Aluno
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

admin.site.register(Escola)
admin.site.register(Aluno)
admin.site.register(Serie)
admin.site.register(NivelEnsino)
admin.site.register(Turno)
admin.site.register(Empresa)
admin.site.register(Localidade)
admin.site.register(Trajeto)
admin.site.register(Periodo)
admin.site.register(UsuarioEscola)


