from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    # Puedes agregar más campos personalizados aquí

    def __str__(self):
        return self.username

# Create your models here.
