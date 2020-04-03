from django.contrib import admin

# Register your models here.
from blog.models import Escola
from blog.models import Aluno

admin.site.register(Escola)
admin.site.register(Aluno)


