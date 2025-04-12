from django.db import models

class Colaborador(models.Model):
    Nome = models.CharField(max_length=100,null=False)
    Idade = models.IntegerField(null=False)
    Aniversario = models.DateField(null=False)
    Cadastro = models.DateField(null=False)
    Ativo = models.BooleanField(null=False,default=True)

class Tipo_EPI(models.Model):
    Tipo = models.CharField(max_length=100)

class EPI(models.Model):
    Descricao = models.CharField(max_length=100)
    Quantidade = models.FloatField(null=False)
    Tipo_EPI = models.ForeignKey(Tipo_EPI, on_delete=models.CASCADE, related_name="epis")

class Emprestimo_EPI(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="emprestimos")
    epi = models.ForeignKey(EPI, on_delete=models.CASCADE, related_name="emprestimos")
    data_devolucao = models.DateField(null=False)

