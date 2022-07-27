from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('Tratamiento', views.tratamientoVista, name='tratamiento'),
    path('Tratamiento/nuevo', views.nuevoTratamiento, name='nuevoTratamiento'),
    path('Tratamiento/editar', views.editarTratamiento, name='editarTratamiento'),
    path('Area', views.area, name='area'),
    path('Area/nuevo', views.nuevaArea, name="nuevaArea")
  
]