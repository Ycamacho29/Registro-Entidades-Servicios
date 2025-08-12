from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
]
