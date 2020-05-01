from collections import defaultdict

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

    escolaSelecionada = UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola
    listaAlunos=[]
    empresaFiltrado = list(Empresa.objects.all())[-1].codigo
    periodoFiltrado = list(Periodo.objects.all())[-1].codigo_mes
    lista2 = []
    if  request.GET.get('empresas'):
        empresaFiltrado = request.GET.get('empresas')
        periodoFiltrado = request.GET.get('periodos')
        #listaAlunos = Aluno.objects.filter(
        #    escola_codigo=UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola)


        if empresaFiltrado > '0':
            try:
                trajetos = Trajeto.objects.filter(cod_empresa=periodoFiltrado)
            except:
                trajeto = None
                #trajeto_codigo = Trajeto.cod_empresa(cod_empresa=empresas)


        listaAlunos = Aluno.objects.filter(
                                            escola_codigo=UsuarioEscola.objects.get(
                                                                                    codigo_usuario=request.user.id
                                                                                    ).cod_escola
                                            )

        listaTrajetos = Trajeto.objects.filter(cod_empresa=empresaFiltrado)


    else:

        listaAlunos = Aluno.objects.filter(
            escola_codigo=UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola)
        listaTrajetos = Trajeto.objects.all()

    periodos = Periodo.objects.all()
    empresas = Empresa.objects.all()

    for aluno in listaAlunos:
            listaAlunosTrajetos = AlunoTrajeto.objects.filter(aluno_codigo=aluno.matricula)
            #if aluno.matricula in listaAlunosTrajetos.values_list('aluno_codigo'):
            #listaTrajetos = all(xvalues_list('matricula') in listaAlunosTrajetos for x in listaAlunos.values_list('matricula'))
            #return render(request, 'views/html/teste.html', {
             #   'listaAlunos': listaAlunos.values_list('matricula'),
            #})
            # listaTrajetos = [trajetos for item in listaTrajetos if all(a not in b for a in trajetos)]
            # listaAlunoTrajetos = [x for x in listaAlunoTrajetos if x in listaTrajetos]
            # listaAlunoTrajetos = filter(lambda listaAlunoTrajetos: listaAlunoTrajetos in listaTrajetos, listaAlunoTrajetos)
            # listaTrajetos = filter(lambda listaTrajetos: listaTrajetos[3] in trajetos, listaTrajetos)
            listaAlunoTrajetos = []

            listaAlunoTrajetos = []

            for alunoTrajeto in listaAlunosTrajetos:
                for trajeto in listaTrajetos:
                    if trajeto.codigo == alunoTrajeto.trajeto_codigo.codigo:
                        # listaAlunoTrajetos.append([alunoTrajeto.trajeto_codigo.cod_saida.nome + " - " + alunoTrajeto.trajeto_codigo.cod_destino.nome])
                        listaAlunoTrajetos.append(alunoTrajeto)

            lista2.append([aluno, listaAlunoTrajetos])

    return render(request, 'views/html/index3.html', {
        'periodos': periodos,
        'empresas': empresas,
        'escolaSelecionada': escolaSelecionada,
        'listaAlunos': lista2,
        'periodoFiltrado': periodoFiltrado,
        'empresaFiltrado': empresaFiltrado,

    })

@login_required(login_url='/login/')
def teste(request):
    ''' listaAlunos = []
    empresaFiltrado = 2
    periodoFiltrado = 0
    #listaAlunoTrajeto = AlunoTrajeto.objects.all()
    listaAlunos = Aluno.objects.filter(
        escola_codigo=UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola)

    lista2 = []
    listaTrajetos = Trajeto.objects.filter(cod_empresa=empresaFiltrado)
    #listaAlunoTrajeto = AlunoTrajeto.objects.filter(aluno_codigo=1, trajeto_codigo=[1, 2])
    listaAlunos = Aluno.objects.filter(
        escola_codigo=UsuarioEscola.objects.get(codigo_usuario=request.user.id).cod_escola)
    for aluno in listaAlunos:
        listaAlunosTrajetos = AlunoTrajeto.objects.filter(aluno_codigo=aluno.matricula)
        #listaTrajetos = [trajetos for item in listaTrajetos if all(a not in b for a in trajetos)]
        #listaAlunoTrajetos = [x for x in listaAlunoTrajetos if x in listaTrajetos]
        #listaAlunoTrajetos = filter(lambda listaAlunoTrajetos: listaAlunoTrajetos in listaTrajetos, listaAlunoTrajetos)
        #listaTrajetos = filter(lambda listaTrajetos: listaTrajetos[3] in trajetos, listaTrajetos)
        listaAlunoTrajetos = []

        for alunoTrajeto in listaAlunosTrajetos:
          listaAlunoTrajetos.append(aluno.nome)
            listaAlunoTrajetos.append(aluno.serie_codigo.serie)
            listaAlunoTrajetos.append(aluno.turno_codigo.descricao)
            for trajeto in listaTrajetos:
                if trajeto.codigo == alunoTrajeto.trajeto_codigo.codigo:
                    #listaAlunoTrajetos.append([alunoTrajeto.trajeto_codigo.cod_saida.nome + " - " + alunoTrajeto.trajeto_codigo.cod_destino.nome])
                    listaAlunoTrajetos.append(trajeto)

        lista2.append([aluno, listaAlunoTrajetos])

    trajetos = Trajeto.objects.filter(cod_empresa=2)
   # lista2 = listaAlunoTrajeto'''


    lista_aluno_codigo = request.POST.getlist('aluno_codigo')
    lista_aluno_trajeto = request.POST.getlist('aluno_trajeto')
    lista_num_passagens = request.POST.getlist('num_passagens')
    return render(request, 'views/html/teste.html', {
         'lista_aluno_codigo': lista_aluno_codigo,
         'lista_aluno_trajeto': lista_aluno_trajeto,
         'lista_num_passagens': lista_num_passagens,
    })


@login_required(login_url='/login/')
@csrf_protect
def savePassagens(request):
    lista_aluno_codigo = request.POST.getlist('lista_aluno_codigo')
    lista_aluno_trajeto = request.POST.getlist('lista_aluno_trajeto')

    data_mes = Periodo.objects.get(codigo_mes=request.POST.getlist('periodos')[0])

    for aluno_codigo in lista_aluno_codigo:
        lista_aluno_trajeto = request.POST.getlist('trajeto_'+aluno_codigo)
        for aluno_trajeto in lista_aluno_trajeto:
            alunoTrajeto = AlunoTrajeto.objects.get(aluno_codigo_id=aluno_codigo,trajeto_codigo_id=aluno_trajeto)
            alunoTrajeto.dt_mes = data_mes
            alunoTrajeto.passagens = request.POST.getlist('num_passagens_' + aluno_codigo + "_" + aluno_trajeto)[0]
            if alunoTrajeto.passagens:
                try:
                    '''return render(request, 'views/html/teste.html', {
                        'request': alunoTrajeto.passagens,
                    })'''
                    alunoTrajeto.save()
                except :
                    messages.error(request, alunoTrajeto)

                ''' try:
                    alunoTrajeto = AlunoTrajeto.objects.filter(aluno_codigo_id=aluno_codigo,
                                                               trajeto_codigo_id=aluno_trajeto).update(
                        dt_mes=data_mes)
    
                    alunoTrajeto = AlunoTrajeto.objects.filter(aluno_codigo_id=aluno_codigo,
                                                               trajeto_codigo_id=aluno_trajeto).update(
                        passagens=request.POST.getlist('num_passagens_' + aluno_codigo + "_" + aluno_trajeto)
                    )
                except :
                    messages.error(request, alunoTrajeto)'''

    return redirect('/index')

def filter_dropdown2(request):
    context = {}
    state = request.GET.get('state')
    city = request.GET.get('city')
    context['form'] = AlunoTrajeto(state, city)
    # Filtro
    q = request.GET.get('district')
    if q:
        q = q.replace('.', '')
        persons = Person.objects.filter(district=str(q))
        context['persons'] = persons
    return render(request, 'filter_dropdown2.html', context)

@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/login')