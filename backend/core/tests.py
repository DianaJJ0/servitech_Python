from django.test import TestCase
from .models import Usuario, Experto

class UsuarioExpertoTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            nombre='Juan',
            apellido='Pérez',
            rol='experto'
        )
        self.experto = Experto.objects.create(
            usuario=self.usuario,
            especialidad='Desarrollo Web',
            sesiones=5,
            calificacion=4.8,
            verificado=True
        )

    def test_usuario_creado(self):
        usuario = Usuario.objects.get(email='test@example.com')
        self.assertEqual(usuario.nombre, 'Juan')
        self.assertEqual(usuario.rol, 'experto')
        self.assertEqual(str(usuario), 'Juan Pérez (experto)')

    def test_experto_creado(self):
        experto = Experto.objects.get(usuario=self.usuario)
        self.assertEqual(experto.especialidad, 'Desarrollo Web')
        self.assertTrue(experto.verificado)
        self.assertEqual(str(experto), 'Juan Pérez - Desarrollo Web')
