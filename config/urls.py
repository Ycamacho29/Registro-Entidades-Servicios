"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('accounts/', include('apps.authentication.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('tipos_entidad/', include('apps.registro_tipo_entidad.urls')),
    path('entidades/', include('apps.registro_entidad.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('roles/', include('apps.roles.urls')),
    path('admin/', admin.site.urls)
]

# Configuración para servir archivos de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
