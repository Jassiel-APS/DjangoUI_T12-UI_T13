# Vamos a crear para el modulo alumnos un formulario que nos permita crear un nuevo alumno.
from .models import Alumno
from django import forms

#Crear una clase por cada formulario que necesitemos.
class alumnoForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    #Definir los metadatos del form clase Meta.
    class Meta:
        #Personalizar el Formulario
        #1) Definir el modelo.
        model = Alumno
        #2) Definir los campos que deben aparecer.
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']
        #3) Atributos de las etiquetas (Widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese el nombre del alumno'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese el apellido del alumno'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese la edad del alumno'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese la matricula del alumno'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese el correo del alumno'
                }
            )
        }

        #4) Personalizar las etiquetas (o los textos que salen a lado de los inputs)
        labels = {
            'nombre': 'Nombre del alumno',
            'apellido': 'Apellido del alumno',
            'edad': 'Edad del alumno',
            'matricula': 'Matricula del alumno',
            'correo': 'Correo del alumno'
        }

        #5) Personalizar los mensajes de error.
        error_messages = {
            'edad': {
                'required': 'La edad no puede estar vacía',
                'invalid': 'Ingresa un valor valido'
            },
            'matricula': {
                'required': 'La matricula no puede estar vacía',
                'invalid': 'Ingresa un valor valido'
            },
            'correo': {
                'required': 'El correo no puede estar vacío',
                'invalid': 'Ingresa un valor valido'
            }
        }