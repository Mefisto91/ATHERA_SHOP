from django.db import models

class PrendaM(models.Model):
    talla = models.CharField(max_length=3)
    color = models.CharField(max_length=20)
    disponible = models.BooleanField(default=True)
    cantidad = models.IntegerField()
    

