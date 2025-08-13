from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
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

    context = {
        'form': form,
        'titulo': 'Crear Nuevo Rol'
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
