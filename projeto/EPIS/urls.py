from django.urls import path
from . import views

urlpatterns = [

    # Colaboradores
    path("Colaboradores/", views.Colaboradores, name="Colaboradores"),
    path("Cadastro_Colaborador/", views.Cadastro_Colaborador, name="cadastrar_colaborador"),
    path("NovoColaborador/", views.NovoColaborador, name="novo_colaborador"),
    path('ExcluirColaborador/<int:Id>/', views.ExcluirColaborador, name='excluir_colaborador'),

    # EPIs
    path('EPIS/', views.EPIS, name="listar_epi"),
    path("CadastroEPI/", views.Cadastro_EPIS, name="cadastrar_epi"),
    path('ExcluirEPI/<int:Id>/', views.ExcluirEPI, name='excluir_epi'),
    path('NovoEPI/', views.NovoEPI, name="novo_epi"),

    # Tipo EPIs
    path("Tipo_EPIS/", views.Tipo_EPIS, name="listar_tipo_epi"),
    path('CadastroTipo_Epis/', views.CadastroTipo_Epis, name="cadastro_tipo_epi"),
    path('excluir_tipo_epi/<int:Id>/', views.ExcluirTipo_EPI, name='excluir_tipo_epi'),
    path('NovoTipo_EPI/', views.NovoTipo_EPI, name="novo_tipo_epi"),

    #Emprestimos de EPI
    path('cadastro_emprestimo/', views.CadastroEmprestimo, name='cadastro_emprestimo'),
    path('Emprestimos/', views.Emprestimos, name='emp_list'),  
    path('novo_emprestimo/', views.NovoEmprestimo, name='novo_emprestimo'),
]
