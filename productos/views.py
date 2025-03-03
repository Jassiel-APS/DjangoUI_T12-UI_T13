from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets #Vamos a crear una vista de varias al mismo tiempo
from rest_framework.renderers import JSONRenderer

class ProductoViewSet(viewsets.ModelViewSet):
    # 1) Permitir saber a que objetos hace referencia
    queryset = Producto.objects.all()
    # 2) Permitir saber como se va a serializar los objetos
    serializer_class = ProductoSerializer
    # 3) Permitir saber como se va a renderizar la respuesta
    renderer_classes = [JSONRenderer] #Solo se va a renderizar en JSON
    # 4) Permitir saber que metodos HTTP vamos a permitir
    # http_method_names = ['GET', 'POST', 'put', 'delete']
