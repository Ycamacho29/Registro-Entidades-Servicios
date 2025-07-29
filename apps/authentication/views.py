'''Vistas de la App de Authentication'''

from django.shortcuts import render, redirect
from django.contrib import messages
from apps.authentication.forms import CustomRegisterForm
# Create your views here.
def register(request):
    '''Vista de Registro'''
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            # user = form.save()
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
