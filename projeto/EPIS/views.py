from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *

#Colaboradores
def Colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request,"Colaborador/colaboradores.html",{"colaboradores": colaboradores})

def Cadastro_Colaborador(request):
    return render(request,"Colaborador/cadastro_colaborador.html")

def NovoColaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/Colaboradores')
    else:
        form = ColaboradorForm()
    
    return render(request, 'Colaborador/cadastro_colaborador.html')

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

def EPIS(request):
    epis = EPI.objects.all()
    return render(request, "EPIS/EPIs.html", {"EPI": epis})

def Cadastro_EPIS(request):
    tipo_epis = Tipo_EPI.objects.all()
    return render(request, "EPIS/cadastro_EPI.html", {"tipo_epis": tipo_epis})

def NovoEPI(request):
    if request.method == 'POST':
        form = EPIForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/EPIS') 

    tipo_epis = Tipo_EPI.objects.all()
    return render(request, 'EPIS/cadastro_EPI.html', {"tipo_epis": tipo_epis})

# Exclui um EPI
def ExcluirEPI(request, Id):
    try:
        epi = EPI.objects.get(id=Id)
        epi.delete()
        return redirect('/EPIS')
    except EPI.DoesNotExist:
        return HttpResponseRedirect('/Erro', status=404)

#Tipo_EPIS

def Tipo_EPIS(request):
    Tipos = Tipo_EPI.objects.all()
    return render(request,"Tipo_EPIS/Tipos_EPI.html",{"Tipo_EPIS": Tipos})
    
def NovoTipo_EPI(request):
    if request.method == 'POST':
        form = Tipo_EPIForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/Tipo_EPIS')
        
    return render(request, 'Tipo_EPIS/cadastroTipo_EPI.html')    

def CadastroTipo_Epis(request):
    return render(request,"Tipo_EPIS/cadastroTipo_EPI.html")

def ExcluirTipo_EPI(request, Id):
    Tipo_EPIs = Tipo_EPI.objects.filter(id=Id).first()
    if Tipo_EPIs:
        Tipo_EPIs.delete() 
        return redirect('/Tipo_EPIS')
    else:
        return HttpResponseRedirect('/Erro', status=404)
    
# Emprestimos de EPi

def CadastroEmprestimo(request):
    colaboradores = Colaborador.objects.all()
    epis = EPI.objects.all()
    situacao_choices = Emprestimo_EPI.SITUACOES
    return render(request, "Emprestimos_EPIS/Cadastro_Emprestimos_EPI.html", {"colaboradores": colaboradores, "epis": epis, 'situacao_choices': situacao_choices,})

def NovoEmprestimo(request):
    if request.method == 'POST':
        form = EmprestimoEPIForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save() 
        return redirect('/Emprestimos')  

    return render(request, 'Emprestimos_EPIS/Cadastro_Emprestimos_EPI.html')

def Emprestimos(request):
    emprestimos = Emprestimo_EPI.objects.all()
    return render(request, 'Emprestimos_EPIS/Emprestimos_EPI.html', {'emprestimos': emprestimos})
  