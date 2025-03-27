from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets #Vamos a crear una vista de varias
from rest_framework.renderers import JSONRenderer

class ProductoViewset(viewsets.ModelViewSet):
    #1) Permite saber a que objeto hago referencia
    queryset = Producto.objects.all()
    #2) Permite serializar los objetos
    serializer_class = ProductoSerializer
    #3) Renderizar las respuestas
    renderer_classes = [JSONRenderer]
    #4) Establecer que métodos puedo usar
    #http_method_names = ['GET', 'POST']


from .forms import productoForm
from django.shortcuts import render
def agregar_producto(request):
    form = productoForm
    return render(request, 'agregar.html', {'form': form})