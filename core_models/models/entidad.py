from django.db import models
from core_models.models.estados import Estado
from core_models.models.municipios import Municipio
from core_models.models.parroquias import Parroquia
from core_models.models.tipo_entidad import TipoEntidad

class Entidad(models.Model):
    nombre = models.CharField(max_length=100, blank=False, unique=True)
    tipo = models.ForeignKey(TipoEntidad, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.PROTECT)
    detalle_direccion = models.TextField()
    punto_referencia = models.TextField(blank=True)
    horario_atencion_lunes = models.TextField(blank=True)
    horario_atencion_martes = models.TextField(blank=True)
    horario_atencion_miercoles = models.TextField(blank=True)
    horario_atencion_jueves = models.TextField(blank=True)
    horario_atencion_viernes = models.TextField(blank=True)
    horario_atencion_sabado = models.TextField(blank=True)
    horario_atencion_domingo = models.TextField(blank=True)
    telefono = models.CharField(max_length=11, blank=True)
    pagina_web = models.URLField(blank=True)
    foto = models.ImageField(upload_to='entidades/fotos/', blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
        db_table = 'entidades'
        indexes = [
            models.Index(fields=['tipo'], name='idx_entidades_tipo'),
            models.Index(fields=['estado', 'municipio', 'parroquia'], name='idx_entidades_ubicacion'),
        ]

    def __str__(self):
        return str(self.nombre)