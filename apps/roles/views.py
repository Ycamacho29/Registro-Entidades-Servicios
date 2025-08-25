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
            return redirect('role_list')
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
            return redirect('role_list')
    else:
        form = RoleEditForm(instance=role)

    context = {
        'form': form,
        'titulo': f'Editar Rol: {role.name}',
        'role_name': role.name
    }
    return render(request, 'roles/editar_rol.html', context)
