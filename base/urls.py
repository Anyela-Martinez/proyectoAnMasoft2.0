"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
<<<<<<< HEAD
from asignatura import views
from base.views import error_404, inicio, inicioAdmin, educacion, manual, modulos, noticias 
=======
from base.views import error_404, inicio, inicioAdmin, educacion, modulos, noticias, manual, contacto

from base.views import logout_user
>>>>>>> 514f61722d84e3d275dab841872a746118a358fa
from django.contrib.auth import  views as auth_views


handler404= error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='pass_reset'),
    path('reiniciar/enviar',auth_views.PasswordResetDoneView.as_view(),name='pass_reset_done'),
    path('reiniciar/<uid64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='pass_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='pass_reset_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', logout_user, name='logout'),
    path('', inicio, name='inicio'),
    path('accounts/login/', inicio, name='inicio'),
    path('adm/', inicioAdmin, name='inicio-admin'),
    path('manual/', manual, name='manual'),
    path('contacto/', contacto, name='contacto'),
    path('modulos/', modulos, name='modulos'),
    path('noticias/', noticias, name='noticias'),
    path('usuarios/', include('usuarios.urls')),
    path('asignatura/', include('asignatura.urls')),
    path('curso/', include('curso.urls')),
    path('docentes/', include('docentes.urls')),
    path('estudiantes/', include('estudiantes.urls')),
    path('eventos/', include('eventos.urls')),
    path('grado/', include('grado.urls')),
    path('preregistro/', include('preregistro.urls')),
    path('publicaciones/', include('publicaciones.urls')),
    path('educacion/', educacion, name='educacion'),
<<<<<<< HEAD
    path('manual/', manual, name='manual'),
]
=======
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
>>>>>>> 514f61722d84e3d275dab841872a746118a358fa
