from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
# Registrar el Path común para las rutas
router.register(r'api', ProductoViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('agregar/', agregar_producto, name='x'),

]

