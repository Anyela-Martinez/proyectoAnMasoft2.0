# Generated by Django 4.1.2 on 2022-11-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grado',
            name='Estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
    ]
