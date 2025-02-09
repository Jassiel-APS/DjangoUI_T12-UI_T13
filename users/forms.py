from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$',
            'title': 'La contraseña debe contener al menos 8 caracteres, una mayúscula, una minúscula y un número',
            'required': True
        })
    )

    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repetir Contraseña',
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$',
            'title': 'La contraseña debe coincidir con la anterior',
            'required': True
        })
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                'title': 'Debes de ingresar un email de la UTEZ',
                'required': True
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'required': True
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido',
                'required': True
            }),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern':  '^(\d{5}[A-Za-z]{2}\d{3})$',
                'title': 'El número de control debe de tener el formato 20223tn073',
                'placeholder': 'Número de control',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'min': 0,
                'max': 100,
                'required': True
            }),
            'tel': forms.TextInput(attrs={  
                'class': 'form-control',
                'placeholder': 'Teléfono',
                'maxlength': 10,
                'minlength': 10,
                'required': True
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9]+@utez\.edu\.mx$', email):
            raise forms.ValidationError('Debes de ingresar un email de la UTEZ')
        return email

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if not re.match(r'^\d{5}[A-Za-z]{2}\d{3}$', control_number):
            raise forms.ValidationError('El número de control debe de tener el formato 20223tn073')
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if not re.match(r'^\d{10}$', tel):
            raise forms.ValidationError('El teléfono debe tener exactamente 10 dígitos')
        return tel

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', password1):
            raise forms.ValidationError('La contraseña debe contener al menos 8 caracteres, una mayúscula, una minúscula y un número')
        return password2

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
            'title': 'Debes ingresar un correo de la UTEZ',
            'required': True
        })
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$',
            'title': 'La contraseña debe contener al menos 8 caracteres, una mayúscula, una minúscula y un número',
            'required': True
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^[a-zA-Z0-9]+@utez\.edu\.mx$', username):
            raise forms.ValidationError('Debes ingresar un correo de la UTEZ')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', password):
            raise forms.ValidationError('La contraseña debe contener al menos 8 caracteres, una mayúscula, una minúscula y un número')
        return password