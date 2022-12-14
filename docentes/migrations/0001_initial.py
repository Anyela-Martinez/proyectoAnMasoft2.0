# Generated by Django 4.1.2 on 2022-12-06 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asignatura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDoc', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PP', 'Pasaporte')], default='CC', max_length=3, verbose_name='Tipo de Documento')),
                ('numDoc', models.CharField(max_length=60, verbose_name='Número de Documento')),
                ('nombres', models.CharField(max_length=60, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('I', 'Indefinido')], default='M', max_length=3, verbose_name='Género')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=40, verbose_name='Dirección')),
                ('correo', models.EmailField(max_length=60, verbose_name='Correo Electrónico')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('jornada', models.CharField(choices=[('MAÑANA', 'Jornada Mañana'), ('TARDE', 'Jornada Tarde')], default='MAÑANA', max_length=10, verbose_name='Jornada')),
                ('foto', models.ImageField(blank=True, default='images/usuarios/default.png', upload_to='images/usuarios')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignatura.asignatura', verbose_name='Asignatura')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario')),
            ],
        ),
    ]
