from django.db import models

# Create your models here.
class TipoDivision(models.Model):
     tipo_division =models.CharField(max_length=250, blank=False, null=False)

     def __str__(self):
        return self.tipo_division