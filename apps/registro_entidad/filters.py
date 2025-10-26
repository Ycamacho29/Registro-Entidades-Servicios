import django_filters
from core_models.models.entidad import Entidad
from core_models.models.tipo_entidad import TipoEntidad
from core_models.models.estados import Estado
from core_models.models.municipios import Municipio
from core_models.models.parroquias import Parroquia

# Definimos las opciones para el filtro booleano 'activo'
BOOLEAN_CHOICES = (  # La opción vacía como placeholder
    ('true', 'Activo'),                # Valor para filtrar por True
    ('false', 'Inactivo'),             # Valor para filtrar por False
)


class EntidadFilter(django_filters.FilterSet):
    # Filtros de texto con búsqueda insensible a mayúsculas
    nombre = django_filters.CharFilter(
        lookup_expr='icontains', label='Nombre de la Entidad')
    telefono = django_filters.CharFilter(
        lookup_expr='icontains', label='Teléfono')

    # Filtro para campos booleanos (activo o inactivo)
    # activo = django_filters.BooleanFilter(
    #     label='Activo',)

    activo = django_filters.ChoiceFilter(
        choices=BOOLEAN_CHOICES,
        method='filter_activo',  # Definiremos el método de filtrado
        label='',
        empty_label="Seleccione El Estatus de la Entidad"
    )

    # Filtros para las relaciones de clave foránea
    tipo = django_filters.ModelChoiceFilter(
        queryset=TipoEntidad.objects.all(),
        label='',
        empty_label="Seleccione Tipo de Entidad"
    )
    estado = django_filters.ModelChoiceFilter(
        queryset=Estado.objects.all(),
        label='',
        empty_label="Seleccione un Estado"
    )
    municipio = django_filters.ModelChoiceFilter(
        queryset=Municipio.objects.all(),
        label='',
        empty_label="Seleccione un Municipio"
    )
    parroquia = django_filters.ModelChoiceFilter(
        queryset=Parroquia.objects.all(),
        label='',
        empty_label="Seleccione una Parroquia"
    )

    class Meta:
        model = Entidad
        fields = [
            'nombre',
            'tipo',
            'estado',
            'municipio',
            'parroquia',
            'activo',
            'telefono',
        ]

    # Método personalizado para manejar el filtrado del campo 'activo'
    def filter_activo(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(activo=True)
        if value == 'false':
            return queryset.filter(activo=False)
        return queryset
