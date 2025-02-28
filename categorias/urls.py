from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/',lista_categorias, name='lista'),
    path('registrar/', agregar_categoria ,name='agregar'),
    path('json/', lista_categorias_html, name='json'),
    path('api/post/', registrar_c, name='post'),

]