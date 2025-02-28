from django.db import models

class Producto(models.Model):  # Cambié a singular por convención
    #Atributos de la clase
    #Mandar a construir un campo de los modelos de Django
    nombre = models.CharField(max_length=100)  # Corrección en max_length
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()

    def __str__(self):  # Corrección en __str__ y añadido ':'
        return self.nombre
