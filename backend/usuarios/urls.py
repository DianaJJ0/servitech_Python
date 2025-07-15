from django.urls import path
from .views import RegistroUsuarioAPI, LoginAPI, PerfilUsuarioAPI

urlpatterns = [
    path('api/registro/', RegistroUsuarioAPI.as_view(), name='api_registro'),
    path('api/login/', LoginAPI.as_view(), name='api_login'),
    path('api/perfil/', PerfilUsuarioAPI.as_view(), name='api_perfil'),
]
