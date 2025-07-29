# En tu forms.py
from django import forms
from core_models.models import TipoEntidad

# Lista de opciones de iconos (puedes expandirla o cargarla desde un archivo/BD)
# Asegúrate de que estas clases CSS existan en tu frontend (ej. Font Awesome)
ICONO_CHOICES = [
    # Servicios de Salud
    ('hospital', 'Hospital / Clínica'),
    ('local_hospital', 'Hospital (alternativo)'),
    ('emergency', 'Emergencias / Primeros Auxilios'),
    ('medication', 'Farmacia / Medicamentos'),

    # Seguridad y Gobierno
    ('local_police', 'Comisaría / Policía'),
    ('gavel', 'Juzgado / Legal'),
    ('fire_truck', 'Estación de Bomberos'),
    ('account_balance', 'Gobierno / Finanzas'),

    # Servicios Automotrices / Mantenimiento
    ('car_repair', 'Taller Mecánico / Reparación de Vehículos'),
    ('build', 'Construcción / Mantenimiento'),
    ('local_gas_station', 'Gasolinera'),

    # Educación
    ('school', 'Escuela / Universidad'),
    ('book', 'Biblioteca / Educación'),

    # Otros Servicios Públicos/Comerciales
    ('store', 'Tienda / Comercio'),
    ('restaurant', 'Restaurante / Comida'),
    ('hotel', 'Hotel / Hospedaje'),
    ('park', 'Parque / Recreación'),
    ('home', 'Vivienda / Residencia'),
    ('public', 'Servicio Público General'),
    ('corporate_fare', 'Oficina / Corporación'),
    ('business', 'Negocio / Empresa'),
    ('phone_in_talk', 'Centro de Llamadas / Atención al Cliente'),
    ('warehouse', 'Almacén'),
    ('fitness_center', 'Gimnasio / Centro Deportivo'),
    ('wash', 'Lavandería'),
    ('pets', 'Veterinaria / Mascotas'),

    # Iconos Genéricos/Comodines
    ('settings', 'Configuración / Servicios Generales'),
    ('place', 'Ubicación / Punto de Interés'),
    ('info', 'Información / Servicios'),
]


class TipoEntidadForm(forms.ModelForm):
    icono_clase = forms.ChoiceField(
        choices=ICONO_CHOICES,
        label="Seleccionar Icono",
        # Clase para estilos de Bootstrap/Material
        widget=forms.Select(attrs={'class': 'form-control'})
    )



    class Meta:
        model = TipoEntidad
        fields = ['nombre', 'icono_clase', 'estatus']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Hospital, Taller'}),
        }
        labels = {
            'nombre': 'Nombre del Tipo de Entidad',
            'estatus': 'Estado (Activo/Inactivo)',  # Etiqueta para el checkbox
        }
