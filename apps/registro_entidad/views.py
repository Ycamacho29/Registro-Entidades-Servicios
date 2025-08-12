from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from apps.registro_entidad.forms import EntidadForm, PersonaContactoFormset
from core_models.models.entidad import Entidad
from core_models.models.municipios import Municipio
from core_models.models.parroquias import Parroquia
from core_models.models.personas import PersonaContacto
from django.db import transaction

# Create your views here.


def index(request):
    entidades = Entidad.objects.all().order_by('nombre')
    context = {
        'segment': 'entidades',
        'entidades': entidades,
    }
    return render(request, 'entidades/entidades.html', context)


def crear_entidad(request):
    if request.method == 'POST':
        # Instanciar el formulario de Entidad con los datos del POST y los archivos
        entidad_form = EntidadForm(request.POST, request.FILES)

        # Instanciar el formset de PersonaContacto con los datos del POST y los archivos
        contacto_formset = PersonaContactoFormset(
            request.POST, request.FILES, prefix='contacto')

        # Validar ambos formularios
        if entidad_form.is_valid() and contacto_formset.is_valid():
            try:
                # Usar una transacción para asegurar que ambos se guarden o ninguno
                with transaction.atomic():
                    # 1. Guardar la Entidad primero
                    entidad = entidad_form.save(commit=False)
                    entidad.save()

                    # 2. Guardar las Personas de Contacto
                    # Iterar sobre los formularios válidos del formset
                    for form in contacto_formset:
                        contacto = form.save(commit=False)
                        if contacto.nombres:  # Solo guardar si hay datos en el formulario
                            contacto.entidad = entidad  # Asignar la entidad al contacto
                            contacto.save()

                    messages.success(
                        request, f'La entidad "{entidad.nombre}" y sus contactos se han creado correctamente.')
                    # Redirige al index de entidades
                    return redirect('index_entidad')

            except Exception as e:
                messages.error(
                    request, f"Ocurrió un error al guardar la información. {e}")

    else:  # GET
        entidad_form = EntidadForm()
        contacto_formset = PersonaContactoFormset(
            queryset=PersonaContacto.objects.none(), prefix='contacto')

    context = {
        'entidad_form': entidad_form,
        'contacto_formset': contacto_formset,
        'titulo': 'Registrar Nueva Entidad y Contactos'
    }
    return render(request, 'entidades/crear_entidad.html', context)


def detalle_entidad(request, pk):
    """
    Muestra los detalles de una entidad específica, incluyendo sus contactos.
    """
    # Obtiene la entidad o devuelve un error 404 si no existe
    entidad = get_object_or_404(Entidad, pk=pk)

    # El campo 'personas_de_contacto' es una relación inversa (ForeignKey en PersonaContacto)
    # y Django la maneja automáticamente como 'personacontacto_set'
    contactos = entidad.contactos.all()

    context = {
        'entidad': entidad,
        'contactos': contactos,
        'titulo': f'Detalle de {entidad.nombre}'
    }
    return render(request, 'entidades/detalle_entidad.html', context)


def editar_entidad(request, pk):
    entidad = get_object_or_404(Entidad, pk=pk)

    if request.method == 'POST':
        entidad_form = EntidadForm(
            request.POST, request.FILES, instance=entidad)
        contacto_formset = PersonaContactoFormset(
            request.POST, request.FILES, instance=entidad, extra=0)  # <--- Cambia `extra=0`

        print(entidad_form.is_valid())
        print(contacto_formset.is_valid())

        # --- DEBUGGER AVANZADO PARA ERRORES DE FORMULARIO Y FORMSET ---
        print("--- ERRORES DEL FORMULARIO DE LA ENTIDAD ---")
        print(entidad_form.errors)

        print("--- ERRORES GLOBALES DEL FORMSET ---")
        print(contacto_formset.non_form_errors())

        print("--- ERRORES INDIVIDUALES DE CADA FORMULARIO EN EL FORMSET ---")
        for i, form in enumerate(contacto_formset):
            print(f"Errores en el formulario de contacto #{i+1}:")
            if form.errors:
                for field, errors in form.errors.items():
                    print(f"  - Campo '{field}': {', '.join(errors)}")
            # --- FIN DEL DEBUGGER ---

        if entidad_form.is_valid() and contacto_formset.is_valid():
            try:
                with transaction.atomic():
                    entidad = entidad_form.save()
                    contacto_formset.save()

                messages.success(
                    request, f'La entidad "{entidad.nombre}" y sus contactos se han actualizado correctamente.')

                return redirect('index_entidad')
            except Exception as e:
                messages.error(
                    request, f"Ocurrió un error al guardar la información. {e}")
    else:
        entidad_form = EntidadForm(instance=entidad)
        contacto_formset = PersonaContactoFormset(
            instance=entidad, extra=0)  # <--- Cambia `extra=0`

    context = {
        'entidad_form': entidad_form,
        'contacto_formset': contacto_formset,
        'titulo': f'Editar Entidad: {entidad.nombre}'
    }
    return render(request, 'entidades/editar_entidad.html', context)


def get_municipios(request, estadoId):
    # Obtiene los municipios del estado seleccionado
    municipios = Municipio.objects.filter(
        estado_id=estadoId).order_by('nombre')

    # Prepara los datos para la respuesta JSON
    data = [{'id': m.id, 'nombre': m.nombre} for m in municipios]

    return JsonResponse(data, safe=False)


def get_parroquias(request, municipioId):
    # Obtiene las parroquias del municipio seleccionado
    parroquias = Parroquia.objects.filter(
        municipio_id=municipioId).order_by('nombre')

    # Prepara los datos para la respuesta JSON
    data = [{'id': p.id, 'nombre': p.nombre} for p in parroquias]

    return JsonResponse(data, safe=False)
