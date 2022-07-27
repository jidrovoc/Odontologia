from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('Paciente',views.pacienteVista,name='paciente'),
    path('Paciente/nuevo', views.nuevoPaciente, name='nuevoPaciente'),
    path('Paciente/editar', views.editarPaciente, name='editarPaciente'),
]