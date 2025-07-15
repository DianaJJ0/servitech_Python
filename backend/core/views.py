def home(request):
    return JsonResponse({'mensaje': '¡Backend Django funcionando!'})
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .models import Usuario, Experto
from .serializers import UsuarioSerializer, ExpertoSerializer

def home(request):
    return JsonResponse({'mensaje': '¡Backend Django funcionando!'})

# Registro de usuario
class RegistroUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({'mensaje': 'Usuario registrado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Login de usuario
class LoginUsuarioView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        usuario = authenticate(request, email=email, password=password)
        if usuario:
            login(request, usuario)
            return Response({'mensaje': 'Login exitoso'}, status=status.HTTP_200_OK)
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)

# Listar y crear expertos
class ExpertoListCreateView(generics.ListCreateAPIView):
    queryset = Experto.objects.all()
    serializer_class = ExpertoSerializer
    permission_classes = [permissions.IsAuthenticated]

# Detalle, actualización y eliminación de experto
class ExpertoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experto.objects.all()
    serializer_class = ExpertoSerializer
    permission_classes = [permissions.IsAuthenticated]
