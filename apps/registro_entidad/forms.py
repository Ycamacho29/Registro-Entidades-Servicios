from django import forms
from core_models.models import *
from django.forms.models import inlineformset_factory, BaseInlineFormSet

# Opciones para los horarios (ej: un selector de 24 horas)
HORA_CHOICES = [('', 'Cerrado')] + \
    [(f'{h:02d}:00', f'{h:02d}:00') for h in range(0, 24)]

# Un TimeInput personalizado para el estilo


class CustomTimeInput(forms.TimeInput):
    input_type = 'time'


class EntidadForm(forms.ModelForm):
    horario_apertura_lunes = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    horario_cierre_lunes = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    cerrado_lunes = forms.BooleanField(
        label="Cerrado", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    horario_apertura_martes = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    horario_cierre_martes = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    cerrado_martes = forms.BooleanField(
        label="Cerrado", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    horario_apertura_miercoles = forms.TimeField(
        widget=CustomTimeInput(attrs={'class': 'form-control'}), required=False)
    horario_cierre_miercoles = forms.TimeField(
        widget=CustomTimeInput(attrs={'class': 'form-control'}), required=False)
    cerrado_miercoles = forms.BooleanField(
        label="Cerrado", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    horario_apertura_jueves = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    horario_cierre_jueves = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    cerrado_jueves = forms.BooleanField(
        label="Cerrado", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    horario_apertura_viernes = forms.TimeField(
        widget=CustomTimeInput(attrs={'class': 'form-control'}), required=False)
    horario_cierre_viernes = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    cerrado_viernes = forms.BooleanField(
        label="Cerrado", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    horario_apertura_sabado = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    horario_cierre_sabado = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    cerrado_sabado = forms.BooleanField(
        label="Cerrado", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    horario_apertura_domingo = forms.TimeField(
        widget=CustomTimeInput(attrs={'class': 'form-control'}), required=False)
    horario_cierre_domingo = forms.TimeField(widget=CustomTimeInput(
        attrs={'class': 'form-control'}), required=False)
    cerrado_domingo = forms.BooleanField(
        label="Cerrado", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    # Campos de llaves foráneas (selects)
    estado = forms.ModelChoiceField(
        queryset=Estado.objects.all().order_by('nombre'),
        empty_label="Seleccione un Estado",
        required=True,  # Puede ser True o False según tu lógica
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    municipio = forms.ModelChoiceField(
        queryset=Municipio.objects.none(),  # Inicialmente vacío, se llenará con JS
        empty_label="Seleccione un Municipio",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    parroquia = forms.ModelChoiceField(
        queryset=Parroquia.objects.none(),  # Inicialmente vacío, se llenará con JS
        empty_label="Seleccione una Parroquia",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tipo = forms.ModelChoiceField(
        # Asegúrate de filtrar si solo quieres activos
        queryset=TipoEntidad.objects.all().order_by('nombre'),
        empty_label="Seleccione un Tipo de Entidad",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Entidad
        fields = [
            'nombre', 'detalle_direccion', 'punto_referencia',
            'horario_atencion_lunes', 'horario_atencion_martes', 'horario_atencion_miercoles',
            'horario_atencion_jueves', 'horario_atencion_viernes', 'horario_atencion_sabado',
            'horario_atencion_domingo',
            'telefono', 'pagina_web', 'activo',
            'estado', 'municipio', 'parroquia', 'tipo',
            'foto'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Hospital Central'}),
            'detalle_direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ej: Avenida Principal, entre calles 5 y 6'}),
            'punto_referencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Frente a la Plaza Bolívar'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: +582121234567'}),
            'pagina_web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ej: https://www.ejemplo.com'}),
            # Para el switch de Material Dashboard
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch'}),
            # Para el input de tipo archivo
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'detalle_direccion': 'Dirección Detallada',
            'punto_referencia': 'Punto de Referencia',
            'activo': 'Activo',
            'telefono': 'Teléfono',
            'pagina_web': 'Página Web',
            'estado': 'Estado',
            'municipio': 'Municipio',
            'parroquia': 'Parroquia',
            'tipo': 'Tipo de Entidad',
            'foto': 'Foto del Local',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 1. Lógica para rellenar los horarios de atención en modo de edición
        if self.instance and self.instance.pk:
            dias_semana = ['lunes', 'martes', 'miercoles',
                           'jueves', 'viernes', 'sabado', 'domingo']
            for day in dias_semana:
                horario_str = getattr(
                    self.instance, f'horario_atencion_{day}', None)
                if horario_str and horario_str != 'Cerrado':
                    try:
                        apertura_str, cierre_str = horario_str.split(' - ')
                        self.initial[f'horario_apertura_{day}'] = apertura_str
                        self.initial[f'horario_cierre_{day}'] = cierre_str
                    except (ValueError, IndexError):
                        pass
                else:
                    self.initial[f'cerrado_{day}'] = True

        # 2. Lógica unificada para los selects anidados (municipio y parroquia)
        estado_id = None
        municipio_id = None

        # Priorizar los datos enviados (POST)
        if self.data:
            try:
                estado_id = int(self.data.get('estado'))
                municipio_id = int(self.data.get('municipio'))
            except (ValueError, TypeError):
                pass

        elif self.instance and self.instance.pk:
            estado_id = self.instance.estado_id
            municipio_id = self.instance.municipio_id

        # Filtra los municipios si hay un estado seleccionado
        if estado_id:
            self.fields['municipio'].queryset = Municipio.objects.filter(
                estado_id=estado_id).order_by('nombre')
        else:
            self.fields['municipio'].queryset = Municipio.objects.none()

        # Filtra las parroquias si hay un municipio seleccionado
        if municipio_id:
            self.fields['parroquia'].queryset = Parroquia.objects.filter(
                municipio_id=municipio_id).order_by('nombre')
        else:
            self.fields['parroquia'].queryset = Parroquia.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        dias_semana = ['lunes', 'martes', 'miercoles',
                       'jueves', 'viernes', 'sabado', 'domingo']

        for day in dias_semana:
            apertura = cleaned_data.get(f'horario_apertura_{day}')
            cierre = cleaned_data.get(f'horario_cierre_{day}')
            cerrado = cleaned_data.get(f'cerrado_{day}')

            # Si el horario no está marcado como cerrado, se validan los campos de hora.
            if not cerrado:
                if apertura and not cierre:
                    # Si hay hora de apertura, pero no de cierre, lanza un error.
                    self.add_error(
                        f'horario_cierre_{day}', "Se debe especificar una hora de cierre.")
                if cierre and not apertura:
                    # Si hay hora de cierre, pero no de apertura, lanza un error.
                    self.add_error(
                        f'horario_apertura_{day}', "Se debe especificar una hora de apertura.")
                # Opcional: Validar que la hora de cierre es posterior a la de apertura.
                if apertura and cierre and apertura > cierre:
                    self.add_error(
                        f'horario_cierre_{day}', "La hora de cierre debe ser posterior a la de apertura.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        dias_semana = ['lunes', 'martes', 'miercoles',
                       'jueves', 'viernes', 'sabado', 'domingo']

        for day in dias_semana:
            apertura = self.cleaned_data.get(f'horario_apertura_{day}')
            cierre = self.cleaned_data.get(f'horario_cierre_{day}')
            cerrado = self.cleaned_data.get(f'cerrado_{day}')

            if cerrado:
                horario_final = "Cerrado"
            elif apertura and cierre:
                # Concatenamos los valores en el formato deseado
                horario_final = f"{apertura.strftime('%H:%M')} - {cierre.strftime('%H:%M')}"
            else:
                # Si no hay valores para apertura y cierre, guardamos como null
                horario_final = None

            # Asignamos el valor concatenado al campo del modelo
            setattr(instance, f'horario_atencion_{day}', horario_final)

        if commit:
            instance.save()
        return instance


class PersonaContactoForm(forms.ModelForm):
    class Meta:
        model = PersonaContacto
        fields = ['nombres', 'apellidos', 'cedula', 'telefono_movil',
                  'telefono_fijo', 'cargo', 'email', 'foto', 'principal']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula de Identidad'}),
            'telefono_movil': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono Móvil'}),
            'telefono_fijo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono Fijo'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'principal': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cedula': 'Cédula',
            'telefono_movil': 'Teléfono Móvil',
            'telefono_fijo': 'Teléfono Fijo',
            'cargo': 'Cargo',
            'email': 'Email',
            'foto': 'Foto',
            'principal': 'Contacto Principal',
        }


# Clase Base del Formset para personalizar el comportamiento
class BasePersonaContactoFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra', 1) 
        super().__init__(*args, **kwargs)
        self.extra = extra # Asignamos el valor al atributo extra

# Creación del Formset para manejar múltiples formularios de contacto
PersonaContactoFormset = forms.inlineformset_factory(
    Entidad,
    PersonaContacto,
    form=PersonaContactoForm,
    formset=BasePersonaContactoFormSet,
    extra=1,  # Muestra un formulario en blanco por defecto
    can_delete=True,  # Permite la eliminación de contactos
    fields=('nombres', 'apellidos', 'cedula', 'telefono_movil',
            'telefono_fijo', 'cargo', 'email', 'foto', 'principal')
)
