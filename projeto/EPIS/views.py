from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
            messages.success(request, 'Cadastro realizado com sucesso!')
            return HttpResponseRedirect('/Cadastro_Colaborador')
        
        else:
            messages.error(request, 'Erro ao cadastrar cliente. Verifique os dados e tente novamente.')
            return HttpResponseRedirect('/Cadastro_Colaborador')
    
    return render(request, 'Colaborador/cadastro_colaborador.html')

def ExcluirColaborador(request, Id):
    colaborador = Colaborador.objects.filter(id=Id).first()
    if colaborador:
        colaborador.delete() 
        return HttpResponseRedirect('/Colaboradores')
    else:
        return HttpResponseRedirect('/Erro', status=404)
    
def Editar_Colaborador(request,Id):
    colaborador = Colaborador.objects.get(id=Id)
    return render(request,'Colaborador/cadastro_colaborador.html',{"colaborador":colaborador})

def Salvar_Colaborador_Editado(request, Id):
    colaborador = get_object_or_404(Colaborador, id=Id)

    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado com sucesso!')
            return HttpResponseRedirect('/Cadastro_Colaborador') 
        else:
            messages.error(request, 'Erro ao Editar. Verifique os dados e tente novamente.')
            return HttpResponseRedirect('/Cadastro_Colaborador') 

    return render(request, 'Colaborador/cadastro_colaborador.html')        

#EPIS

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
            messages.success(request, 'Cadastro realizado com sucesso!')
            return HttpResponseRedirect('/Cadastro_EPI')
        else:
            messages.error(request, 'Erro ao cadastrar EPI. Verifique os dados e tente novamente.')
            return HttpResponseRedirect('/Cadastro_EPI')

    tipo_epis = Tipo_EPI.objects.all()
    return render(request, 'EPIS/cadastro_EPI.html', {"tipo_epis": tipo_epis})

def ExcluirEPI(request, Id):
    try:
        epi = EPI.objects.get(id=Id)
        epi.delete()
        return redirect('/EPIS')
    except EPI.DoesNotExist:
        return HttpResponseRedirect('/Erro', status=404)
    
def Editar_EPI(request,Id):
    epi = EPI.objects.get(id=Id)
    tipo_epis = Tipo_EPI.objects.all()
    return render(request,"EPIS/cadastro_EPI.html",{"epi": epi, "tipo_epis": tipo_epis})

def Salvar_EPI_Editado(request, Id):
    epi = get_object_or_404(EPI, id=Id)
    tipo_epis = Tipo_EPI.objects.all()

    if request.method == 'POST':
        form = EPIForm(request.POST, instance=epi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado com sucesso!')
            return HttpResponseRedirect('/Cadastro_EPI') 
        else:
            messages.error(request, 'Erro ao Editar. Verifique os dados e tente novamente.')
            return HttpResponseRedirect('/Cadastro_EPI') 

    return render(request, 'EPIS/cadastro_EPI.html', {'epi': epi, "tipo_epis": tipo_epis})    

#Tipo_EPIS

def Tipo_EPIS(request):
    Tipos = Tipo_EPI.objects.all()
    return render(request,"Tipo_EPIS/Tipos_EPI.html",{"Tipo_EPIS": Tipos})
    
def NovoTipo_EPI(request):
    if request.method == 'POST':
        form = Tipo_EPIForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Cadastro realizado com sucesso!')
            return HttpResponseRedirect('/Cadastro_Tipo_Epis')
        else:
            messages.error(request, 'Erro ao cadastrar Tipo de EPI. Verifique os dados e tente novamente.')
            return HttpResponseRedirect('/Cadastro_Tipo_Epis')
        
    return render(request, 'Tipo_EPIS/cadastroTipo_EPI.html')    

def CadastroTipo_Epis(request):
    return render(request,"Tipo_EPIS/cadastroTipo_EPI.html")

def Editar_Tipo_EPI(request,Id):
    tipo_epi = Tipo_EPI.objects.get(id=Id)
    return render(request,"Tipo_EPIS/cadastroTipo_EPI.html",{"tipo_epi": tipo_epi})

def Salvar_Tipo_EPI_Editado(request, Id):
    tipo_epi = get_object_or_404(Tipo_EPI, id=Id)

    if request.method == 'POST':
        form = Tipo_EPIForm(request.POST, instance=tipo_epi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado com sucesso!')
            return HttpResponseRedirect('/Cadastro_Tipo_Epis') 
        else:
            messages.error(request, 'Erro ao Editar. Verifique os dados e tente novamente.')
            return HttpResponseRedirect('/Cadastro_Tipo_Epis') 

    return render(request, 'Tipo_EPIS/cadastroTipo_EPI.html', {'tipo_epi': tipo_epi})

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
    situacao_choices = [choice for choice in Emprestimo_EPI.SITUACOES if choice[1] in ['Emprestado', 'Em Uso','Fornecido']]
    return render(request, "Emprestimos_EPIS/Cadastro_Emprestimos_EPI.html", {"colaboradores": colaboradores, "epis": epis, 'situacao_choices': situacao_choices,})

def NovoEmprestimo(request):
    if request.method == 'POST':
        form = EmprestimoEPIForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save() 
            messages.success(request, 'Cadastro realizado com sucesso!')
            return HttpResponseRedirect('/Cadastro_Emprestimo')
        else:
            messages.error(request, 'Erro ao cadastrar empréstimo. Verifique os dados e tente novamente.')
            return HttpResponseRedirect('/Cadastro_Emprestimo')

    return render(request, 'Emprestimos_EPIS/Cadastro_Emprestimos_EPI.html')

def Emprestimos(request):
    emprestimos = Emprestimo_EPI.objects.all()
    return render(request, 'Emprestimos_EPIS/Emprestimos_EPI.html', {'emprestimos': emprestimos})

def Editar_Emprestimos(request,Id):
    emprestimo = get_object_or_404(Emprestimo_EPI, id=Id)    
    colaboradores = get_object_or_404(Colaborador, id=emprestimo.colaborador.id)
    epis = get_object_or_404(EPI, id=emprestimo.epi.id)    
    situacao_choices = [choice for choice in Emprestimo_EPI.SITUACOES if choice[1] not in ['Emprestado', 'Em Uso', 'Fornecido']]

    return render(request,'Emprestimos_EPIS/Cadastro_Emprestimos_EPI.html',{"emprestimo":emprestimo,"colaboradores": colaboradores, "epis": epis, 'situacao_choices': situacao_choices,})

def Salvar_Emprestimos_Editado(request, Id):
    emprestimo = get_object_or_404(Emprestimo_EPI, id=Id)

    if request.method == 'POST':
        form = EmprestimoEPIForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado com sucesso!')
            return HttpResponseRedirect('/Cadastro_Emprestimo') 
        else:
            messages.error(request, 'Erro ao Editar. Verifique os dados e tente novamente.')
            return HttpResponseRedirect('/Cadastro_Emprestimo') 

    return render(request, 'Emprestimos_EPIS/Cadastro_Emprestimos_EPI.html')        
  