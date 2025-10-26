from collections import defaultdict
from itertools import groupby
from operator import attrgetter
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
from .forms import RoleCreateForm, RoleEditForm
from django.contrib import messages

# Vista para listar todos los roles


@login_required
def index(request):
    roles = Group.objects.all().order_by('name')
    context = {
        'segment': 'roles',
        'roles': roles
    }
    return render(request, 'roles/index_rol.html', context)

# Vista para crear un nuevo rol con permisos


@login_required
# @permission_required('auth.add_group') # Descomentar para requerir permiso
def crear_rol(request):
    if request.method == 'POST':
        form = RoleCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El rol se ha creado correctamente.')
            return redirect('index_roles')
    else:
        form = RoleCreateForm()

    # Prepara los permisos para agruparlos en la plantilla
    all_permissions = Permission.objects.all().order_by(
        'content_type__app_label', 'content_type__model')
    grouped_permissions = {}
    for ct, perms in groupby(all_permissions, key=attrgetter('content_type')):
        app_name = ct.app_label
        model_name = ct.model.replace('_', ' ').capitalize()
        # Nombre más legible para el usuario
        grouped_permissions[f"{app_name} | {model_name}"] = list(perms)

    context = {
        'form': form,
        'titulo': 'Crear Nuevo Rol',
        'grouped_permissions': grouped_permissions,  # Pasamos los permisos agrupados
    }
    return render(request, 'roles/crear_rol.html', context)

# Vista para editar un rol existente


@login_required
# @permission_required('auth.change_group') # Descomentar para requerir permiso
def editar_rol(request, pk):
    role = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        form = RoleEditForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'El rol "{role.name}" ha sido actualizado.')
            return redirect('index_roles')
    else:
        form = RoleEditForm(instance=role)

    # --- LÓGICA DE AGRUPACIÓN DE PERMISOS ---
    # 1. Obtener los permisos del formulario
    # Usamos el queryset del campo para obtener todos los permisos disponibles
    all_permissions = form.fields['permissions'].queryset

    # 2. Inicializar el diccionario de grupos
    # defaultdict crea automáticamente una lista vacía para las nuevas claves
    grouped_permissions = defaultdict(list)

    # 3. Obtener los permisos actualmente seleccionados en el rol
    # Esto es crucial para marcar las casillas como 'checked'
    selected_permissions_ids = role.permissions.values_list('id', flat=True)

    # 4. Iterar y agrupar
    for perm in all_permissions:
        group_name = str(perm.content_type)

        permission_label = perm.name

        # Crear un objeto de opción para el template
        permission_choice = {
            'value': perm.id,
            'label': permission_label,
            'is_selected': perm.id in selected_permissions_ids,
            'id_for_label': f'id_permissions_{perm.id}'
        }

        grouped_permissions[group_name].append(permission_choice)

    context = {
        'form': form,
        'titulo': f'Editar Rol: {role.name}',
        'role_name': role.name,
        'grouped_permissions': dict(grouped_permissions),
    }
    return render(request, 'roles/editar_rol.html', context)
