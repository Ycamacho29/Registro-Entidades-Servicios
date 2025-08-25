import django_filters
from core_models.models.entidad import Entidad
from core_models.models.tipo_entidad import TipoEntidad
from core_models.models.estados import Estado
from core_models.models.municipios import Municipio
from core_models.models.parroquias import Parroquia


class EntidadFilter(django_filters.FilterSet):
    # Filtros de texto con búsqueda insensible a mayúsculas
    nombre = django_filters.CharFilter(
        lookup_expr='icontains', label='Nombre de la Entidad')
    telefono = django_filters.CharFilter(
        lookup_expr='icontains', label='Teléfono')

    # Filtro para campos booleanos (activo o inactivo)
    activo = django_filters.BooleanFilter(label='Activa')

    # Filtros para las relaciones de clave foránea
    tipo = django_filters.ModelChoiceFilter(
        queryset=TipoEntidad.objects.all(),
        label='Tipo de Entidad'
    )
    estado = django_filters.ModelChoiceFilter(
        queryset=Estado.objects.all(),
        label='Estado'
    )
    municipio = django_filters.ModelChoiceFilter(
        queryset=Municipio.objects.all(),
        label='Municipio'
    )
    parroquia = django_filters.ModelChoiceFilter(
        queryset=Parroquia.objects.all(),
        label='Parroquia'
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
