from django import forms
from .models import *

# Formulário para Colaborador
class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['Nome', 'Idade', 'Aniversario', 'Cadastro']
        widgets = {
            'Aniversario': forms.DateInput(attrs={'type': 'date'}),
            'Cadastro': forms.DateInput(attrs={'type': 'date'})
        }

# Formulário para EPI
class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['Descricao', 'Quantidade', 'Tipo_EPI']
        widgets = {
            'Tipo_EPI': forms.Select(),  # Dropdown para escolher o Tipo de EPI
        }

# Formulário para Tipo_EPI
class Tipo_EPIForm(forms.ModelForm):
    class Meta:
        model = Tipo_EPI
        fields = ['Tipo']

class EmprestimoEPIForm(forms.ModelForm):
    class Meta:
        model = Emprestimo_EPI
        fields = ['colaborador', 'epi', 'data_devolucao']
        
    colaborador = forms.ModelChoiceField(queryset=Colaborador.objects.all(), required=True)
    epi = forms.ModelChoiceField(queryset=EPI.objects.all(), required=True)
    data_devolucao = forms.DateField(widget=forms.SelectDateWidget(), required=True)
