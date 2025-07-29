from django.db import models
from core_models.models.municipios import Municipio

class Parroquia(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    estatus = models.CharField(max_length=1, default='A')
    creado_en = models.DateField(auto_now_add=True)
    modificado_en = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'
        db_table = 'parroquias'
        indexes = [
            models.Index(fields=['municipio'], name='idx_parroquias_municipio'),
        ]

    def __str__(self):
        return str(f"{self.nombre} ({self.municipio.nombre})")