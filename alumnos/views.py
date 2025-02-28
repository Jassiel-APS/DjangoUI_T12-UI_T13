from .models import Alumno
from .serializers import AlumnoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from django.shortcuts import render
from .forms import alumnoForm

class AlumnoViewSet(viewsets.ModelViewSet):
    # 1) Permitir saber a que objetos hace referencia
    queryset = Alumno.objects.all()
    # 2) Permitir saber como se va a serializar los objetos
    serializer_class = AlumnoSerializer
    # 3) Permitir saber como se va a renderizar la respuesta
    renderer_classes = [JSONRenderer] #Solo se va a renderizar en JSON
    # 4) Permitir saber que metodos HTTP vamos a permitir
    # http_method_names = ['GET', 'POST', 'put', 'delete']

def alumnos_view(request):
    form = alumnoForm()
    return render(request, 'agregar_a.html', {'form': form})