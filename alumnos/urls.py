from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
# Registrar el path comun para las rutas
router.register(r'api', AlumnoViewSet)

urlpatterns = [
    path('', alumnos_view, name='alumnos'),
    path('', include(router.urls)),
]