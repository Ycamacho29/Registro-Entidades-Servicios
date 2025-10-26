from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.utils.translation import gettext_lazy as _  

# Formulario para crear un nuevo usuario


class CustomUserCreationForm(UserCreationForm):
    # 1. Definir el campo del Rol/Grupo
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        label=_("Rol del Usuario"),
        empty_label=_("Seleccione un rol"),
        required=True,  # Lo hacemos obligatorio
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

            # 4. Obtener el rol seleccionado del campo 'role'
            role_id = self.cleaned_data.get('role')
            if role_id:
                user.groups.add(role_id)

        return user

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
