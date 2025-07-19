from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # ...otros campos personalizados...
