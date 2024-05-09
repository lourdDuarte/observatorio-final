from django.db import models
from Año.models import Año
from Mes.models import Mes
from TipoValor.models import TipoValor

# Create your models here.
class Ipc(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    tipo_valor = models.ForeignKey(TipoValor, on_delete=models.CASCADE)
    mes_anterior = models.CharField(max_length=250, blank=False, null=False)
    mes_año_anterior = models.CharField(max_length=250, blank=False, null=False)
    dic_mes_anterior = models.CharField(max_length=250, blank=False, null=False)
    var_mensual = models.CharField(max_length=250, blank=False, null=False)


   