from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.IntegerField(null=True, blank=True)  # Cambiado a IntegerField
    precio_venta = models.IntegerField(null=True, blank=True)  # Cambiado a IntegerField
    stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre
