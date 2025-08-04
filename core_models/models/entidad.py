from django.db import models
from core_models.models.estados import Estado
from core_models.models.municipios import Municipio
from core_models.models.parroquias import Parroquia
from core_models.models.tipo_entidad import TipoEntidad


class Entidad(models.Model):
    nombre = models.CharField(
        max_length=100, blank=False, unique=True, verbose_name="Nombre de la Entidad")
    tipo = models.ForeignKey(TipoEntidad, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.PROTECT)
    detalle_direccion = models.TextField(verbose_name="Detalle de Dirección")
    punto_referencia = models.TextField(
        max_length=255, blank=True, null=True, verbose_name="Punto de Referencia")
    horario_atencion_lunes = models.TextField(
        max_length=50, blank=True, null=True, default="Cerrado", verbose_name="Horario Lunes")
    horario_atencion_martes = models.TextField(
        max_length=50, blank=True, null=True, default="Cerrado", verbose_name="Horario Martes")
    horario_atencion_miercoles = models.TextField(
        max_length=50, blank=True, null=True, default="Cerrado", verbose_name="Horario Miercoles")
    horario_atencion_jueves = models.TextField(
        max_length=50, blank=True, null=True, default="Cerrado", verbose_name="Horario Jueves")
    horario_atencion_viernes = models.TextField(
        max_length=50, blank=True, null=True, default="Cerrado", verbose_name="Horario Viernes")
    horario_atencion_sabado = models.TextField(
        max_length=50, blank=True, null=True, default="Cerrado", verbose_name="Horario Sabado")
    horario_atencion_domingo = models.TextField(
        max_length=50, blank=True, null=True, default="Cerrado", verbose_name="Horario Domingo")
    telefono = models.CharField(
        max_length=11, blank=True, null=True, verbose_name="Teléfono del Local",)
    pagina_web = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Página Web")
    foto = models.ImageField(upload_to='entidades/foto_entidad/',
                             blank=True, verbose_name="Foto de la Entidad")
    activo = models.BooleanField(default=True, verbose_name="Activa")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
        db_table = 'entidades'
        indexes = [
            models.Index(fields=['tipo'], name='idx_entidades_tipo'),
            models.Index(fields=['estado', 'municipio',
                         'parroquia'], name='idx_entidades_ubicacion'),
        ]

    def __str__(self):
        return str(self.nombre)
