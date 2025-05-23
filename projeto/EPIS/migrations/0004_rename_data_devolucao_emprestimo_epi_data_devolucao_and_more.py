# Generated by Django 5.2 on 2025-04-12 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EPIS', '0003_remove_epi_tipo_epi_epi_tipo_epi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo_epi',
            old_name='Data_Devolucao',
            new_name='data_devolucao',
        ),
        migrations.RenameField(
            model_name='emprestimo_epi',
            old_name='Data_Emprestimo',
            new_name='data_emprestimo',
        ),
        migrations.RenameField(
            model_name='emprestimo_epi',
            old_name='Quantidade_EPI',
            new_name='quantidade_epi',
        ),
        migrations.RemoveField(
            model_name='emprestimo_epi',
            name='Id_Colaborador',
        ),
        migrations.RemoveField(
            model_name='emprestimo_epi',
            name='Id_EPI',
        ),
        migrations.AddField(
            model_name='emprestimo_epi',
            name='colaborador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos', to='EPIS.colaborador'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo_epi',
            name='epi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos', to='EPIS.epi'),
            preserve_default=False,
        ),
    ]
