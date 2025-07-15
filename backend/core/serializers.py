from rest_framework import serializers
from .models import Usuario, Experto

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'email', 'password', 'rol', 'estado', 'fecha_registro']

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario

class ExpertoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Experto
        fields = ['id', 'usuario', 'especialidad', 'sesiones', 'calificacion', 'verificado', 'fecha_registro', 'estado']
