

from django.db import models
from core_models.models.estados import Estado


class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False, unique=False)
    estatus = models.CharField(max_length=1, default='A')
    creado_en = models.DateField(auto_now_add=True)
    modificado_en = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        db_table = 'municipios'
        indexes = [
            models.Index(fields=['estado'], name='idx_municipios_estado'),
        ]

    def __str__(self):
        return str(f"{self.nombre} ({self.estado.nombre})")
