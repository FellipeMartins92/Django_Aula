from django.urls import path
from . import views

urlpatterns = [

    # Colaboradores
    path("Colaboradores/", views.Colaboradores, name="Colaboradores"),
    path('Excluir_Colaborador/<int:Id>/', views.ExcluirColaborador, name='Excluir_Colaborador'),
    path("Cadastro_Colaborador/", views.Cadastro_Colaborador, name="Cadastro_Colaborador"),
    path("Novo_Colaborador/", views.NovoColaborador, name="Novo_Colaborador"),    
    path('Editar_Colaborador/<int:Id>/', views.Editar_Colaborador, name='Editar_Colaborador'),
    path('Salvar_Colaborador_Editado/<int:Id>/', views.Salvar_Colaborador_Editado, name='Salvar_Colaborador_Editado'),

    # EPIs
    path('EPIS/', views.EPIS, name="EPIS"),
    path('Excluir_EPI/<int:Id>/', views.ExcluirEPI, name='Excluir_EPI'),
    path("Cadastro_EPI/", views.Cadastro_EPIS, name="Cadastro_EPI"),
    path('Novo_EPI/', views.NovoEPI, name="Novo_EPI"),
    path('Editar_EPI/<int:Id>/', views.Editar_EPI, name='Editar_EPI'),
    path('Salvar_EPI_Editado/<int:Id>/', views.Salvar_EPI_Editado, name='Salvar_EPI_Editado'),

    # Tipo EPIs
    path("Tipo_EPIS/", views.Tipo_EPIS, name="Tipo_EPIS"),
    path('Excluir_Tipo_EPI/<int:Id>/', views.ExcluirTipo_EPI, name='Excluir_Tipo_EPI'),
    path('Cadastro_Tipo_Epis/', views.CadastroTipo_Epis, name="Cadastro_Tipo_Epis"),
    path('NovoTipo_EPI/', views.NovoTipo_EPI, name="NovoTipo_EPI"),
    path('Editar_Tipo_Epis/<int:Id>/', views.Editar_Tipo_EPI, name='Editar_Tipo_Epis'),
    path('Salvar_Tipo_EPI_Editado/<int:Id>/', views.Salvar_Tipo_EPI_Editado, name='Salvar_Tipo_EPI_Editado'),

    #Emprestimos de EPI
    path('Cadastro_Emprestimo/', views.CadastroEmprestimo, name='Cadastro_Emprestimo'),
    path('Emprestimos/', views.Emprestimos, name='Emprestimos'),  
    path('Novo_Emprestimo/', views.NovoEmprestimo, name='Novo_Emprestimo'),
    path('Editar_Emprestimo/<int:Id>/', views.Editar_Emprestimos, name='Editar_Emprestimo'),
    path('Salvar_Emprestimo_Editado/<int:Id>/', views.Salvar_Emprestimos_Editado, name='Salvar_Emprestimo_Editado'),    
]
