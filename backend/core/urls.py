
from django.urls import path
from .views import home, RegistroUsuarioView, LoginUsuarioView, ExpertoListCreateView, ExpertoDetailView

urlpatterns = [
    path('', home, name='home'),
    path('api/registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('api/login/', LoginUsuarioView.as_view(), name='login_usuario'),
    path('api/expertos/', ExpertoListCreateView.as_view(), name='expertos_list_create'),
    path('api/expertos/<int:pk>/', ExpertoDetailView.as_view(), name='experto_detail'),
]
