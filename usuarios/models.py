
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    class TipoDoc(models.TextChoices):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')
    tipoDoc=models.CharField(max_length=3, choices=TipoDoc.choices , default=TipoDoc.CC, verbose_name="Tipo de Documento") 

    numDoc=models.CharField(max_length=60, verbose_name="Número de Documento")

    nombres=models.CharField(max_length=60, verbose_name="Nombres")

    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")

    class Jornada(models.TextChoices):
        JM='MAÑANA', _('Jornada Mañana')
        JT='TARDE', _('Jornada Tarde')
    jornada=models.CharField(max_length=10,choices=Jornada.choices , default=Jornada.JM, verbose_name="Jornada")

    telefono=models.CharField(max_length=20, verbose_name="Teléfono") 

    direccion=models.CharField(max_length=40, verbose_name="Dirección") 

    correo=models.EmailField(max_length=40, verbose_name="Correo Electrónico") 

    class Genero(models.TextChoices):
        M='M', _('Masculino')
        F='F', _('Femenino')
        I='I', _('Indefinido')
    genero=models.CharField(max_length=3,choices=Genero.choices, default=Genero.M, verbose_name="Género")

    class Rol(models.TextChoices):
        ADMIN='ADMIN', _('Administrador')
        DIRECTIVO='DIRECTIVO', _('Directivo')
        SECRETARIA='SECRETARIA', _('Secretaria')
    rol=models.CharField(max_length=10,choices=Rol.choices, default=Rol.ADMIN, verbose_name="Rol")
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    foto=models.ImageField(upload_to='images/usuarios',blank=True, default='images/usuarios/default.png')

    user=models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self)->str:
        return "%s %s" %(self.nombres, self.apellidos) 
