from django.db import models
from core_models.models.entidad import Entidad

class PersonaContacto(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='contactos')
    nombres = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    cedula = models.CharField(max_length=10, unique=True, blank=True, null=True, verbose_name="Cédula de Identidad")
    telefono_movil = models.CharField(max_length=11, verbose_name="Teléfono Móvil")
    telefono_fijo = models.CharField(max_length=11, blank=True, verbose_name="Teléfono Fijo")
    cargo = models.CharField(max_length=80, blank=True)
    foto = models.ImageField(upload_to='entidades/persona_contacto/', blank=True)
    email = models.EmailField(blank=True)
    principal = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Persona de Contacto'
        verbose_name_plural = 'Personas de Contacto'
        db_table = 'persona_contacto'
        indexes = [
            models.Index(fields=['entidad'], name='idx_persona_entidad'),
            models.Index(fields=['cedula'], name='idx_persona_cedula'),
        ]

    def __str__(self):
        return str(f"{self.nombres} {self.apellidos} ({self.entidad.nombre})")