from django import forms
from .models import *

# Formulário para Colaborador
class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['Nome', 'Idade', 'Aniversario']
        widgets = {
            'Nome': forms.TextInput(attrs={'type': 'text'}),
            'Idade': forms.NumberInput(attrs={'type': 'number'}),
            'Aniversario': forms.DateInput(attrs={'type': 'date'})
        }

# Formulário para EPI
class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['Descricao', 'Tipo_EPI']
        widgets = {
            'Descricao': forms.TextInput(attrs={'type': 'text'}),
            'Tipo_EPI': forms.Select(),  
        }

# Formulário para Tipo_EPI
class Tipo_EPIForm(forms.ModelForm):
    class Meta:
        model = Tipo_EPI
        fields = ['Tipo']
        widgets = {
            'Tipo': forms.TextInput(attrs={'type': 'text'})
        }

class EmprestimoEPIForm(forms.ModelForm):
    class Meta:
        model = Emprestimo_EPI
        fields = ['colaborador', 'epi', 'data_devolucao', 'situacao','data_emprestimo']
        
    colaborador = forms.ModelChoiceField(queryset=Colaborador.objects.all(), required=True)
    epi = forms.ModelChoiceField(queryset=EPI.objects.all(), required=True)
    data_emprestimo = forms.DateField(widget=forms.SelectDateWidget(), required=False)
    data_devolucao = forms.DateField(widget=forms.SelectDateWidget(), required=False)
    situacao = forms.ChoiceField(choices = Emprestimo_EPI.SITUACOES) 
