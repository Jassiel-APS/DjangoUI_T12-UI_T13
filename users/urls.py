from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter
from django.shortcuts import render
from .views import *
from django.urls import path, include

router = SimpleRouter()
router.register(r'api', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #Este es el Path para iniciar sesión
    path('token/', CustomTokenObtainPairView.as_view(), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh"),
    path('form/', CustomUserFormAPI.as_view(), name="form"),
]