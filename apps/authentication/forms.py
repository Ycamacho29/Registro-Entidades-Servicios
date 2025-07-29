# from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

# class LoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
#         'class': 'form-control'
#     }))


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Nombre de Usuario'
        self.fields['password'].label = 'Clave'

        # Personaliza los campos
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
        })


User = get_user_model()


class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        # Campos adicionales que quieras incluir
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalización de campos existentes
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
        })
        # Si agregaste el campo email (recomendado)
        if 'email' in self.fields:
            self.fields['email'].widget.attrs.update({
                'class': 'form-control',
                'required': True
            })
        # Mejora las etiquetas (labels)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmación de contraseña"
