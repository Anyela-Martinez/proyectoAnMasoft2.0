# Generated by Django 4.1.1 on 2022-10-20 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignatura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='nombreAsig',
            field=models.CharField(default=2, max_length=60, verbose_name='Nombre de Asignatura'),
            preserve_default=False,
        ),
    ]