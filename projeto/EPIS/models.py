from django.db import models
from django.utils.timezone import now

class Colaborador(models.Model):
    Nome = models.CharField(max_length=100,null=False)
    Idade = models.IntegerField(null=False)
    Aniversario = models.DateField(null=False)
    Cadastro = models.DateField(default=now,null=False)
    Ativo = models.BooleanField(null=False,default=True)

class Tipo_EPI(models.Model):
    Tipo = models.CharField(null=False,max_length=100)

class EPI(models.Model):
    Descricao = models.CharField(null=False,max_length=100)
    Tipo_EPI = models.ForeignKey(Tipo_EPI, on_delete=models.CASCADE, related_name="epis")

class Emprestimo_EPI(models.Model):
    SITUACOES = {
    ("1", "Emprestado"),
    ("2", "Em Uso"),
    ("3", "Fornecido"),
    ("4", "Devolvido"),
    ("5", "Danificado"),
    ("6", "Perdido"),
}
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="emprestimos")
    epi = models.ForeignKey(EPI, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField(null=True,blank=True)
    data_devolucao = models.DateField(null=True,blank=True)
    situacao = models.CharField(max_length=3, choices=SITUACOES)

