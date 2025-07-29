from django.db import models


class Estado(models.Model):
    nombre = models.CharField(max_length=20, blank=False, unique=True)
    estatus = models.CharField(max_length=1, default='A')
    creado_en = models.DateField(auto_now_add=True)
    modificado_en = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'estados'

    def __str__(self):
        return str(self.nombre)
