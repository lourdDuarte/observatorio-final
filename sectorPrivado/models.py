from django.db import models
from Año.models import Año
from Mes.models import Mes
from TipoValor.models import TipoValor




class TipoEstacionalidad(models.Model):
   tipo = models.CharField(max_length=250, blank=False, null=False)

   def __str__(self):
        return self.tipo
   
class RamaActividad(models.Model):
    nombre_rama = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.nombre_rama

# Models Asalariados
class AsalariadosRegistrados(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    tipo_estacionalidad = models.ForeignKey(TipoEstacionalidad, on_delete=models.CASCADE)
    cantidad_registrado = models.CharField(max_length=250, blank=False, null=False)
    dif_intermensual = models.CharField(max_length=250, blank=False, null=False)
    var_intermensual = models.CharField(max_length=250, blank=False, null=False)
    dif_interanual = models.CharField(max_length=250, blank=False, null=False)
    var_interanual = models.CharField(max_length=250, blank=False, null=False)



class AsalariadosRama(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    tipo_rama = models.ForeignKey(RamaActividad, on_delete=models.CASCADE)
    cantidad_registrado = models.CharField(max_length=250, blank=False, null=False)
    var_intertrimestral = models.CharField(max_length=250, blank=False, null=False)


# Models Remuneracion
class Remuneracion(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    tipo_estacionalidad = models.ForeignKey(TipoEstacionalidad, on_delete=models.CASCADE)
    remuneracion_promedio = models.CharField(max_length=250, blank=False, null=False)
    var_intermensual = models.CharField(max_length=250, blank=False, null=False)
    var_interanual = models.CharField(max_length=250, blank=True, null=True)

class RemuneracionRama(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    tipo_estacionalidad = models.ForeignKey(TipoEstacionalidad, on_delete=models.CASCADE)
    tipo_rama = models.ForeignKey(RamaActividad, on_delete=models.CASCADE)
    var_intermensual = models.CharField(max_length=250, blank=False, null=False)




