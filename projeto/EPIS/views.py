from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from .forms import *
from .models import *
from .serializers import *


def Home(request):
    return render(request,"Home.html")

#Colaboradores
def Colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request,"colaboradores.html",{"colaboradores": colaboradores})

def Cadastro_Colaborador(request):
    return render(request,"cadastro_colaborador.html")

def NovoColaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/Colaboradores')
    else:
        form = ColaboradorForm()
    
    return render(request, 'cadastro_colaborador.html', {'form': form})

def ExcluirColaborador(request, Id):
    colaborador = Colaborador.objects.filter(id=Id).first()
    if colaborador:
        colaborador.delete() 
        return HttpResponseRedirect('/Colaboradores')
    else:
        return HttpResponseRedirect('/Erro', status=404)

#EPIS

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import EPI, Tipo_EPI
from .forms import EPIForm

# Exibe a lista de EPIs
def EPIS(request):
    epis = EPI.objects.all()
    return render(request, "EPIs.html", {"EPI": epis})

# Exibe a página de cadastro de EPI
def Cadastro_EPIS(request):
    tipo_epis = Tipo_EPI.objects.all()  # Passa todos os tipos de EPI para o template
    return render(request, "cadastro_EPI.html", {"tipo_epis": tipo_epis})

# Cria um novo EPI
def NovoEPI(request):
    if request.method == 'POST':
        form = EPIForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo EPI
            return redirect('/EPIS')  # Redireciona para a lista de EPIs após o sucesso
    else:
        form = EPIForm()  # Inicializa o formulário vazio

    tipo_epis = Tipo_EPI.objects.all()  # Passa todos os tipos de EPI para o template
    return render(request, 'cadastro_EPI.html', {'form': form, "tipo_epis": tipo_epis})

# Exclui um EPI
def ExcluirEPI(request, Id):
    try:
        epi = EPI.objects.get(id=Id)  # Usa get() para pegar o EPI com o Id especificado
        epi.delete()  # Exclui o EPI
        return redirect('/EPIS')  # Redireciona para a lista de EPIs
    except EPI.DoesNotExist:
        return HttpResponseRedirect('/Erro', status=404)  # Caso o EPI não exista

#Tipo_EPIS

def Tipo_EPIS(request):
    Tipos = Tipo_EPI.objects.all()
    return render(request,"Tipos_EPI.html",{"Tipo_EPIS": Tipos})
    
def NovoTipo_EPI(request):
    if request.method == 'POST':
        form = Tipo_EPIForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/Tipo_EPIS')
    else:
        form = Tipo_EPIForm()    
    return render(request, 'cadastroTipo_EPI.html', {'form': form})    

def CadastroTipo_Epis(request):
    return render(request,"cadastroTipo_EPI.html")

def ExcluirTipo_EPI(request, Id):
    Tipo_EPIs = Tipo_EPI.objects.filter(id=Id).first()
    if Tipo_EPIs:
        Tipo_EPIs.delete() 
        return HttpResponseRedirect('/Tipo_EPIS')
    else:
        return HttpResponseRedirect('/Erro', status=404)
    
# Emprestimos de EPi

def CadastroEmprestimo(request):
    colaboradores = Colaborador.objects.all()
    epis = EPI.objects.all()
    return render(request, "Cadastro_Emprestimos_EPI.html", {"colaboradores": colaboradores, "epis": epis})

def NovoEmprestimo(request):
    if request.method == 'POST':
        form = EmprestimoEPIForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save() 
        return redirect('/Emprestimos')  
    else:
        form = EmprestimoEPIForm()  

    return render(request, 'Cadastro_Emprestimos_EPI.html', {'form': form})

def Emprestimos(request):
    emprestimos = Emprestimo_EPI.objects.all()
    return render(request, 'Emprestimos_EPI.html', {'emprestimos': emprestimos})
  