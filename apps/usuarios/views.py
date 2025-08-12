from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserActivationForm
from django.contrib import messages

# Create your views here.
# views.py


# Vista para listar todos los usuarios
@login_required
def index(request):
    users = User.objects.all().order_by('username')
    context = {
        'segment': 'usuarios',
        'users': users
    }
    return render(request, 'usuarios/index.html', context)

# Vista para crear un nuevo usuario


@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El usuario se ha creado correctamente.')
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
        'titulo': 'Crear Nuevo Usuario'
    }
    return render(request, 'usuarios/crear_usuarios.html', context)

# Vista para activar o desactivar un usuario


@login_required
def editar_usuario(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserActivationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            if user.is_active:
                messages.success(
                    request, f'El usuario "{user.username}" ha sido activado.')
            else:
                messages.warning(
                    request, f'El usuario "{user.username}" ha sido desactivado.')
            return redirect('user_list')
    else:
        form = UserActivationForm(instance=user)

    context = {
        'form': form,
        'user': user,
        'titulo': f'Editar Usuario: {user.username}'
    }
    return render(request, 'usuarios/editar_usuario.html', context)
