from django.db import models

producto_status = [
    ('Disponible', 'DISPONIBLE'),
    ('No Disponible', 'NO DISPONIBLE'),
    ('Descontinuado', 'DESCONTINUADO')
]
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=250)
    talla = models.CharField(max_length=30)
    color = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    estado = models.CharField(
        null=False, blank=False,
        choices=producto_status,
        max_length=15

    )

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contraseña = models.CharField(max_length=20)
    
