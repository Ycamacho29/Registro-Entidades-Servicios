from django.urls import path
from apps.registro_entidad import views

urlpatterns = [
    path('', views.index, name="index_entidad"),
    path('crear/', views.crear_entidad, name="crear_entidad"),
    path('editar/<int:pk>/', views.editar_entidad, name="editar_entidad"),
    path('detalle/<int:pk>/', views.detalle_entidad, name="detalles_entidad"),
    path('entidades/<int:pk>/pdf/', views.generate_entidad_pdf, name='entidad_pdf_descargar'),
    path('api/municipios/<int:estadoId>/',
         views.get_municipios, name='api_municipios'),
    path('api/parroquias/<int:municipioId>/',
         views.get_parroquias, name='api_parroquias'),
]
