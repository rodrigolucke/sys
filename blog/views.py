from django.db.models import Manager
from .models import Periodo, UsuarioEscola, Empresa, Escola, Aluno
from pprint import pprint
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def loginNoAdmin(request):
    return render(request,'admin/loginNoAdmin.html')


@csrf_protect
def loginUser(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index/')
        else:
            messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
            messages.error(request, 'Se não possui cadastro contate o administrador do sistema, no caso o Rodrigo.')
            messages.error(request, 'Contato: 51 99371-4915')
    return redirect('/login/')

@login_required(login_url='/login/')
@csrf_protect
def index2(request):
    pet = ""#Aluno.filter(active=True)
    periodos = Periodo.objects.all()
    empresas = Empresa.objects.all()
    escolaSelecionada = UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola
    listaAlunos = Aluno.objects.filter(
        escola_codigo=UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola)
    pprint(escolaSelecionada)
    return render(request, 'views/html/dados2.html', {
        'periodos': periodos,
        'empresas': empresas,
        'escolaSelecionada': escolaSelecionada,
        'listaAlunos': listaAlunos,
    })
@login_required(login_url='/login/')
@csrf_protect
def index3(request):
    periodos = Periodo.objects.all()
    empresas = Empresa.objects.all()
    escolaSelecionada = UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola
    listaAlunos =Aluno.objects.filter(escola_codigo=UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola)
    pprint(escolaSelecionada)
    return render(request, 'views/html/index3.html', {
        'periodos':periodos,
        'empresas':empresas,
        'escolaSelecionada':escolaSelecionada,
        'listaAlunos':listaAlunos,
    })


@login_required(login_url='/login/')
@csrf_protect
def index(request):
    p = Periodo.objects.all()

    return render(request, 'views/html/index.html', {'periodos':p})

@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/login')