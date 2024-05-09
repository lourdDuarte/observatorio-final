from django.db import models
from Ipc.models import Ipc
from IpcTipoDivision.models import TipoDivision

# Create your models here.
class IpcDivision(models.Model):
     ipc = models.ForeignKey(Ipc, on_delete=models.CASCADE)
     tipo_division = models.ForeignKey(TipoDivision, on_delete= models.CASCADE)
     valor_mensual = models.CharField(max_length=250, blank=False, null=False)
     valor_interanual = models.CharField(max_length=250, blank=False, null=False)