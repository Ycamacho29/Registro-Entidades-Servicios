from django.urls import path
from apps.registro_entidad import views

urlpatterns = [
    path('', views.index, name="index_entidad"),
    path('crear/', views.crear_entidad, name="crear_entidad"),
]
