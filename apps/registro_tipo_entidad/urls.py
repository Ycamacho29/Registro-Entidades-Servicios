from django.urls import path
from apps.registro_tipo_entidad import views

urlpatterns = [
    path('', views.index, name='index_tipo_entidad'),
    path('create', views.crear_tipo_entidad, name='crear_tipo_entidad'),
    path('update/<int:pk>/', views.editar_tipo_entidad,
         name='actualizar_tipo_entidad'),
]
