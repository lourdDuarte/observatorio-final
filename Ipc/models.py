from django.db import models
from Año.models import Año
from Mes.models import Mes
from TipoValor.models import TipoValor

# Create your models here.
class TipoDivision(models.Model):
     tipo_division =models.CharField(max_length=250, blank=False, null=False)

     def __str__(self):
        return self.tipo_division

class Ipc(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    mes_anterior = models.CharField(max_length=250, blank=False, null=False)
    mes_año_anterior = models.CharField(max_length=250, blank=False, null=False)
    dic_año_anterior = models.CharField(max_length=250, blank=False, null=False)


class IpcDivision(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    tipo_division = models.ForeignKey(TipoDivision, on_delete= models.CASCADE)
    valor_mensual = models.CharField(max_length=250, blank=False, null=False)
    valor_interanual = models.CharField(max_length=250, blank=False, null=False)