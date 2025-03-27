from django.db import models

class Detalles_Producto(models.Model):
    descripción = models.TextField(max_length=400)
    fecha_caducidad = models.DateField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

from categorias.models import Categoria

class Producto(models.Model):  # Cambié a singular por convención
    #Atributos de la clase
    #Mandar a construir un campo de los modelos de Django
    nombre = models.CharField(max_length=100)  # Corrección en max_length
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()

    #Relacion 1:1
    detlles_producto = models.OneToOneField(
        Detalles_Producto, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE
    )

    #Relacion 1:M
    categoria = models.ForeignKey(
        Categoria, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE
    )

    #Relacion M:M
    proveedor = models.ManyToManyField(
        Proveedor,
        null=True, 
        blank=True
    )

    def __str__(self):  # Corrección en __str__ y añadido ':'
        return self.nombre


