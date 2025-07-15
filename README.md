# Servitech Python

Servitech es una plataforma integral para conectar usuarios con expertos en tecnología, ofreciendo asesorías personalizadas, mensajería, videollamadas y gestión de pagos. El proyecto está compuesto por un backend en Django (API RESTful) y un frontend estático moderno, integrados para una experiencia profesional y segura.

## Estructura del Proyecto

```
servitech_Python/
├── backend/                # Backend Django (API REST, modelos, autenticación)
│   ├── core/               # App principal (puede contener lógica común)
│   ├── usuarios/           # App de usuarios (registro, login, perfil)
│   ├── settings.py         # Configuración global Django
│   └── ...
├── frontend/               # Frontend estático (HTML, CSS, JS, componentes)
│   ├── componentes/        # Componentes reutilizables (header, footer, navbar)
│   ├── assets/             # Recursos estáticos (css, js, imágenes)
│   ├── index.html          # Landing page
│   ├── mensajes.html       # Chat y mensajería
│   ├── registro.html       # Registro de usuarios
│   ├── login.html          # Login de usuarios
│   └── ...
├── manage.py               # Comando de gestión Django
├── README.md               # Documentación del proyecto
└── ...
```

## Tecnologías principales
- **Backend:** Python 3.12, Django 4.2, Django REST Framework, SQLite3
- **Frontend:** HTML5, CSS3, JavaScript ES6, EJS (migrado a HTML estático), Bootstrap (opcional)
- **Integración:** Fetch API, localStorage, JWT (autenticación), CORS

## Funcionalidades principales
- Registro y autenticación de usuarios (API REST, JWT)
- Gestión de perfiles de usuario
- Búsqueda y listado de expertos por categorías
- Mensajería en tiempo real (Socket.IO, chat)
- Videollamadas integradas (Jitsi Meet)
- Pasarela de pagos (PayU, PSE, Nequi, Daviplata)
- Panel de administración para gestión de usuarios, expertos y publicaciones
- Componentes reutilizables (header, footer, navbar) cargados dinámicamente

## Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/DianaJJ0/servitech_Python.git
cd servitech_Python
```

### 2. Backend (Django)
- Crear y activar un entorno virtual:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Instalar dependencias:
  ```bash
  pip install -r requirements.txt
  ```
- Realizar migraciones y crear superusuario:
  ```bash
  python manage.py migrate
  python manage.py createsuperuser
  ```
- Ejecutar el servidor:
  ```bash
  python manage.py runserver 8080
  ```

### 3. Frontend (estático)
- Desde la carpeta `frontend`, iniciar un servidor web simple:
  ```bash
  cd frontend
  python3 -m http.server 8000
  ```
- Acceder a la app en: [http://localhost:8000/index.html](http://localhost:8000/index.html)

## Endpoints principales (API REST)
- `POST /usuarios/api/registro/` — Registro de usuario
- `POST /usuarios/api/login/` — Login de usuario (retorna token)
- `GET /usuarios/api/perfil/` — Perfil del usuario autenticado
- `GET /expertos/api/` — Listado de expertos
- `POST /mensajeria/api/mensajes/` — Enviar mensaje
- `POST /pagos/api/` — Procesar pago

## Estructura de componentes frontend
- `componentes/header.html` — Header y navegación principal
- `componentes/footer.html` — Footer y enlaces legales
- `assets/js/` — Scripts para validación, autenticación, chat, etc.
- `assets/css/` — Estilos globales y de componentes

## Notas y buenas prácticas
- Todas las rutas de recursos en el frontend deben ser relativas (`./assets/...`, `./componentes/...`) para compatibilidad con servidores estáticos.
- Los componentes HTML se cargan dinámicamente con `fetch` para mantener DRY y facilitar el mantenimiento.
- El backend y frontend pueden ejecutarse de forma independiente para facilitar el desarrollo y pruebas.
- Para producción, se recomienda servir los archivos estáticos desde un CDN o servidor optimizado.

## Autores y contacto
- Diana Carolina Jimenez — [GitHub](https://github.com/DianaJJ0)
- Contribuciones y sugerencias son bienvenidas.

---

© 2025 Servitech. Todos los derechos reservados.
