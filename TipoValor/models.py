from django.db import models

# Create your models here.
class TipoValor(models.Model):
    valor = models.CharField(max_length=200, blank=False, null=False)


    def __str__(self):
        return self.valor