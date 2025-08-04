from django.shortcuts import redirect, render
from django.contrib import messages
from apps.registro_entidad.forms import EntidadForm, PersonaContactoFormset
from core_models.models.entidad import Entidad
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
        contacto_formset = PersonaContactoFormset(request.POST, request.FILES, prefix='contacto')

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
                        if contacto.nombre: # Solo guardar si hay datos en el formulario
                            contacto.entidad = entidad # Asignar la entidad al contacto
                            contacto.save()
                    
                    messages.success(request, f'La entidad "{entidad.nombre}" y sus contactos se han creado correctamente.')
                    return redirect('lista_entidades') # Redirige a la lista de entidades
            
            except Exception as e:
                messages.error(request, f"Ocurrió un error al guardar la información. {e}")
                
    else: # GET
        entidad_form = EntidadForm()
        contacto_formset = PersonaContactoFormset(queryset=PersonaContacto.objects.none(), prefix='contacto')
        
    context = {
        'entidad_form': entidad_form,
        'contacto_formset': contacto_formset,
        'titulo': 'Registrar Nueva Entidad y Contactos'
    }
    return render(request, 'entidades/crear_entidad.html', context)
