from django.db import models
from Año.models import Año
from Mes.models import Mes
from TipoValor.models import TipoValor


# Create your models here.
class AsalariadosRegistrados(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    cantidad_sin_estacionalidad = models.CharField(max_length=250, blank=False, null=False)
    dif_intermensual = models.CharField(max_length=250, blank=False, null=False)
    dif_interanual = models.CharField(max_length=250, blank=False, null=False)
    var_intermensual = models.CharField(max_length=250, blank=False, null=False)
    var_interanual = models.CharField(max_length=250, blank=False, null=False)

class Remuneracion(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    promedio_estacionalidad = models.CharField(max_length=250, blank=False, null=False)
    var_intermensual = models.CharField(max_length=250, blank=False, null=False)
    var_interanual = models.CharField(max_length=250, blank=False, null=False)


class RamaActividad(models.Model):
    rama = models.CharField(max_length=250, blank=False, null=False)


class AsalariadosRama(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    rama = models.ForeignKey(RamaActividad, on_delete=models.CASCADE)
    sin_estacionalidad = models.CharField(max_length=250, blank=False, null=False)
    con_estacionalidad = models.CharField(max_length=250, blank=False, null=False)
    


class RemuneracionRama(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    rama = models.ForeignKey(RamaActividad, on_delete=models.CASCADE)
    registrado_con_estacionalidad = models.CharField(max_length=250, blank=False, null=False)