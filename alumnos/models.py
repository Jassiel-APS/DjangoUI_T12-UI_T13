from django.db import models

class Alumno(models.Model):
    #Atributos de la clase
    # Mandar a construir un campo de los modelos de Django
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre