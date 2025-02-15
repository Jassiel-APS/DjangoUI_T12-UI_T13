# Vamos a crear formularios para cada modulo de la app/modulo
from .models import Producto
from django import forms

#Crear una clase por cada formulario que necesitemos.
class productoForm(forms.ModelForm):
    #Definir los metadatos del form clase Meta.
    class Meta:
        #Personalizar el Formulario
        #1) Definir el modelo.
        model = Producto
        #2) Definir los campos que deben aparecer.
        fields = ['nombre', 'precio', 'imagen']
        #3) Atributos de las etiquetas (Widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            )
        }

        #4) Personalizar las etiquetas (o los textos que salen a lado de los inputs)
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen'
        }

        #5) Personalizar los mensajes de error.
        error_messages = {
            'precio': {
                'required': 'El precio no puede estar vacío',
                'invalid': 'Ingresa un valor valido'
            }
        }