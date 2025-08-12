from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Formulario para crear un nuevo usuario
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

# Formulario para editar el estado de un usuario (activo/inactivo)
class UserActivationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_active']
        labels = {
            'is_active': 'Estado del Usuario (Activo/Inactivo)'
        }
        widgets = {
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }