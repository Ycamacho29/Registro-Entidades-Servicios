from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_roles'),
    path('crear/', views.crear_rol, name='crear_rol'),
    path('editar/<int:pk>/', views.editar_rol, name='editar_rol'),
]
