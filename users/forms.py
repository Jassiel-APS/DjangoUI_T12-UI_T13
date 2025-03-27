from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel','password1', 'password2']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Debes ingresar un correo de la UTEZ',
                    'required': True
                }
            ),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$',
                'title': 'Ingresa solo letras y espacios en el nombre.',
                'required': True,
                'minlength': 2,
                'maxlength': 50,
            }
            ),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$',  
                'title': 'Ingresa solo letras y espacios en el apellido.',
                'required': True,
                'minlength': 2,
                'maxlength': 50,
            }
            ),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '^[A-Za-z0-9]{10}$',  
                'title': 'Ingresa una matrícula válida de exactamente 10 caracteres alfanuméricos.',
                'required': True,
            }
            ),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 18,  
                'max': 100,  
                'title': 'Ingresa una edad válida (entre 18 y 100 años).',
                'required': True,
            }
            ),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '^[0-9]{10}$',
                'title': 'Ingresa un número de teléfono válido (10 dígitos).',
                'required': True,
            }
            ),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'pattern': '^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&?])[A-Za-z\d!@#$%&?]{8,}$',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un símbolo especial (!@#$%&?).',
                'required': True,
            }
            ),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'title': 'Confirma tu contraseña.',
                'required': True,
            }
            ),
        }
class CustomUserLoginForm(AuthenticationForm):
    email = forms.CharField(label="Correo electrónico", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match('^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$', email):
            raise forms.ValidationError("El correo debe terminar el @utez.edu.mx")
        return email
    
    def clean_password1(self):
        password = self.cleanned_data.get("password1")
        if not re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&?])[A-Za-z\d!@#$%&?]{8,}$', password):
            raise forms.ValidationError("La contraseña debe contener al menos 8 carácteres entre Mayúsculas, minúsculas y símbolos especiales.")
        return password
    
    def clean_control_number(self):
        control_number = self.cleanned_data.get("control_number")
        if not re.match('^[A-Za-z0-9]{10}$', control_number):
            raise forms.ValidationError("La matrícula debe tener exactamente 10 caracteres alfanuméricos.")
        return control_number
    
    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        if not re.match('^[0-9]{10}$', tel):
            raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
        return tel
    
    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18 or age > 100:
            raise forms.ValidationError("La edad debe estar entre 18 y 100 años.")
        return age
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data