from .models import CustomUser
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer

# Clase que maneja las vistas GET, POST, PUT, DELETE
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = CustomUserSerializer

    # Variables para autenticación
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated()]
        return []


from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    """ Vista que genera y envía el token JWT """
    serializer_class = CustomTokenObtainPairSerializer


from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm  # Corregido el nombre de la importación
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView  # Corregido 'vies' a 'views'


class CustomUserFormAPI(APIView):
    def get(self, request, *args, **kwargs):
        """ Obtiene los campos del formulario y los devuelve como JSON """
        form = CustomUserCreationForm()
        fields = {
            field: {
                'label': form[field].label,
                'input': form[field].field.widget.attrs,  # Corregido 'widgets' a 'widget'
                'type': form[field].field.widget.input_type,
            }
            for field in form.fields
        }
        return Response(fields)

    def post(self, request, *args, **kwargs):
        """ Recibe los datos del formulario, valida y crea un nuevo usuario """
        form = CustomUserCreationForm(data=request.data)
        if form.is_valid():
            user_data = form.cleaned_data
            User = get_user_model()
            user = User.objects.create_user(
                email=user_data['email'],
                password=user_data['password1'],  # Django usa password1 para creación
                name=user_data['name'],
                surname=user_data['surname'],
                control_number=user_data['control_number'],
                age=user_data['age'],
                tel=user_data['tel'],
            )
            return Response({'message': 'Usuario creado con éxito'}, status=status.HTTP_201_CREATED)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)