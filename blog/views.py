from django.db.models import Manager
from .models import Periodo, UsuarioEscola, Empresa, Escola, Aluno, AlunoTrajeto, Trajeto
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
def index(request):
    try:
        periodos = Periodo.objects.all()
        empresas = Empresa.objects.all()
        escolaSelecionada = UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola
        listaAlunos = Aluno.objects.filter(
            escola_codigo=UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola)
    except Periodo.DoesNotExist:
        periodos = None
        empresas = None
        escolaSelecionada = None
        listaAlunos = None

    return render(request, 'views/html/index3.html', {
        'periodos': periodos,
        'empresas': empresas,
        'escolaSelecionada': escolaSelecionada,
        'listaAlunos': listaAlunos,
    })

@login_required(login_url='/login/')
@csrf_protect
def savePassagens(request):
    lista_aluno_codigo = request.POST.getlist('aluno_codigo')
    lista_aluno_trajeto = request.POST.getlist('aluno_trajeto')
    lista_num_passagens = request.POST.getlist('num_passagens')

    data_mes = Periodo.objects.get(codigo_mes=1)
    sucesso = 1
    for aluno_codigo,trajeto_codigo,num_passagens in zip(lista_aluno_codigo, lista_aluno_trajeto, lista_num_passagens):
        aluno =  Aluno.objects.get(matricula=aluno_codigo)
        alunoTrajeto = AlunoTrajeto()
        alunoTrajeto.dt_mes = data_mes
        alunoTrajeto.trajeto_codigo = Trajeto.objects.get(codigo=trajeto_codigo)
        alunoTrajeto.aluno_codigo = aluno
        alunoTrajeto.passagens = num_passagens
        try:
            alunoTrajeto.save()
        except :
            sucesso = 0
            messages.error(request, 'Erro ao salvar o aluno: ' + aluno.nome)

    return redirect('/index')
@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/login')