from django import forms
from django.contrib.auth.models import Group, Permission

# Formulario para crear un nuevo rol


class RoleCreateForm(forms.ModelForm):
    # El campo de permisos usa un widget de checkbox
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Permisos del Rol"
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']
        labels = {
            'name': 'Nombre del Rol',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulario para editar un rol existente


class RoleEditForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Permisos del Rol"
    )

    class Meta:
        model = Group
        fields = ['permissions']
        # El campo 'name' no se incluye para que no se pueda cambiar al editar
