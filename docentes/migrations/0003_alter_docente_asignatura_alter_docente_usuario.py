# Generated by Django 4.1.2 on 2022-12-06 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('asignatura', '0001_initial'),
        ('docentes', '0002_alter_docente_correo_alter_docente_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='asignatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asignatura.asignatura', verbose_name='Asignatura'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario'),
        ),
    ]
