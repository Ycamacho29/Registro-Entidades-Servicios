from django.db import models


class TipoEntidad(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)

    icono_clase = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Clase CSS del Icono",
        help_text="Ej: fas fa-hospital, fa fa-wrench. Consulta la documentación "
        "de Font Awesome o tu librería de iconos."
    )

    estatus = models.BooleanField(default=True, verbose_name="Estatus")

    creado_en = models.DateField(auto_now_add=True)
    modificado_en = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Tipo de Entidad'
        verbose_name_plural = 'Tipos de Entidad'
        db_table = 'tipo_entidad'

    def __str__(self):
        return str(self.nombre)
