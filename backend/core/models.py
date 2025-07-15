from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (
        ('cliente', 'Cliente'),
        ('experto', 'Experto'),
        ('admin', 'Administrador'),
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=10, choices=ROLES, default='cliente')
    estado = models.CharField(max_length=20, default='activo')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rol})"

class Experto(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='experto')
    especialidad = models.CharField(max_length=100)
    sesiones = models.PositiveIntegerField(default=0)
    calificacion = models.FloatField(default=0)
    verificado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='activo')

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido} - {self.especialidad}"
