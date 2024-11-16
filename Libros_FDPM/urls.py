from django.urls import path
from . import views  

urlpatterns = [
    path('crear/', views.crear_libro, name='crear_libro'),
    path('', views.listar_libros, name='listar_libros'),  # Asegúrate de que esta vista esté definida
]
