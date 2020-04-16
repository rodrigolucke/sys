# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Aluno
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
    pet = ""#Aluno.filter(active=True)
    return render(request, 'views/html/dados2.html', {'pet':pet})

@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/login')