from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from apps.registro_tipo_entidad.forms import TipoEntidadForm
from core_models.models.tipo_entidad import TipoEntidad

# Create your views here.


def index(request):
    tipos_entidad = TipoEntidad.objects.all().order_by('nombre')
    context = {
        'segment': 'tipos_entidad',
        'tipos_entidad': tipos_entidad,
    }
    return render(request, 'tipos_entidad/tipos_entidad.html', context)


def crear_tipo_entidad(request):
    if request.method == 'POST':
        form = TipoEntidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, '¡El tipo de entidad se ha creado correctamente!')

            # Redirige a una página de éxito o a la lista de tipos de entidad
            return redirect('index_tipo_entidad')
    else:
        form = TipoEntidadForm()

    context = {
        'form': form,
        'titulo': 'Crear Nuevo Tipo de Entidad'
    }
    return render(request, 'tipos_entidad/crear_tipo_entidad.html', context)


def editar_tipo_entidad(request, pk):
    # Obtiene el objeto o lanza 404
    tipo_entidad = get_object_or_404(TipoEntidad, pk=pk)

    if request.method == 'POST':
        # Pasa la instancia existente
        form = TipoEntidadForm(request.POST, instance=tipo_entidad)
        if form.is_valid():
            form.save()
            messages.success(
                request, '¡El tipo de entidad se ha actualizado correctamente!')
            # Redirige a la lista después de editar
            return redirect('index_tipo_entidad')
    else:
        # Carga el formulario con los datos existentes
        form = TipoEntidadForm(instance=tipo_entidad)

    context = {
        'form': form,
        # Título dinámico
        'titulo': f'Editar Tipo de Entidad: {tipo_entidad.nombre}',
        'tipo_entidad': tipo_entidad,  # Pasa el objeto para usarlo si es necesario
    }
    return render(request, 'tipos_entidad/editar_tipo_entidad.html', context)
