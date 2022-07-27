import logging
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import *


urlpatterns=[
    path('', inicio ,name='principal'),
    path('accounts/login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('Login', logout_then_login, name='logout'),
    #path('Sistema', views.validarIngreso, name="validarUsuario"),
    path('Inicio',login_required(views.dashboard), name='dashboard'),
    # path('nosotros', views.nosotros, name='nosotros'),
    path('Paciente',login_required(views.pacienteVista),name='paciente'),
    path('Paciente/busqueda', login_required(views.busquedaPaciente), name='busquedaPaciente'),
    path('Paciente/nuevo', login_required(views.nuevoPaciente), name='nuevoPaciente'),
    path('RegistrarPaciente', login_required(views.registrarPaciente), name='registroPaciente'),
    path('EliminarPaciente/<int:id>',login_required(views.eliminarPaciente), name='eliminarPaciente'),
    path('Paciente/editar/<int:id>', login_required(views.editarPaciente), name='editarPaciente'),
    # path('Paciente/actualizado',views.guardarEdicionPaciente, name="guardarEdicionPaciente"),
    path('Tratamiento', login_required(views.tratamientoVista), name='tratamiento'),
    path('Tratamiento/busqueda', login_required(views.busquedaTratamiento), name='busquedaTratamiento'),
    path('Tratamiento/nuevo', login_required(views.nuevoTratamiento), name='nuevoTratamiento'),
    path('Tratamiento/editar/<int:id>', login_required(views.editarTratamiento), name='editarTratamiento'),
    path('RegistrarTratamiento', login_required(views.registrarTratamiento), name="registroTratamiento"),
    path('Tratamiento/eliminar/<int:id>', login_required(views.eliminarTratamiento), name="eliminarTratamiento"),
    path('Area', login_required(views.area), name='area'),
    path('Area/busqueda', login_required(views.busquedaArea), name='busquedaArea'),
    path('Area/nuevo', login_required(views.nuevaArea), name="nuevaArea"),
    path('RegistrarArea', login_required(views.registrarArea), name='registroArea'),
    path('Area/editar/<int:id>', login_required(views.editarArea), name="editarArea"),
    path('EliminarArea/<int:id>', login_required(views.eliminarArea), name="eliminarArea"),
    path('Historial',login_required(views.historia),name='historial'),
    path('Historial/busqueda',login_required(views.busquedaHistorial), name='busquedaHistorial'),
    path('Actualizar',login_required(views.actualizar), name='actualizar'),
    path('Historial/nuevo/<int:id>', login_required(views.nuevaHistoria), name='nuevaHistoria'),
    path('Historial/alergias/<int:id>', login_required(views.alergiaVista), name='alergia'),
    path('GuardarAlergia', login_required(views.guardarAlergia), name="guardarAlergia"),
    path('Historia/odontograma/<int:id>/<int:idHistorial>', login_required(views.odontogramaVista), name="odontograma"),
    path('Historia/odontograma/visualizar/<int:id>/<int:idHistorial>/<int:idOdontogra>', login_required(views.visualizarOdontograma), name="visualizarOdontograma"),
    path('Historia/diagnostico/<int:id>/<int:idHistorial>', login_required(views.diagnosticoVista), name="diagnosticoVista"),
    path('Historia/tratamiento/<int:id>/<int:idHistorial>', login_required(views.tratamientosRealizadosVista), name="tratamientosRealizadosVista"),
    
    path('Doctores', login_required(views.doctorVista), name="doctor"),
    path('Doctor/busqueda', login_required(views.busquedaDoctor), name='busquedaDoctor'),
    path('Doctores/nuevo', login_required(views.nuevoDoctor), name="nuevoDoctor"),
    path('RegistrarDoctor', login_required(views.registrarDoctor), name="registroDoctor"),
    path('Doctor/editar/<int:id>', login_required(views.editarDoctor), name='editarDoctor'),
    path('EliminarDoctor/<int:id>',login_required(views.eliminarDoctor), name='eliminarDoctor'),
    path('Cita', login_required(views.citaVista), name='cita'),
    path('Cita/busqueda', login_required(views.busquedaCita), name='busquedaCita'),
    path('Cita/nueva', login_required(views.nuevaCita), name="nuevaCita"),
    path('RegistrarCita',login_required(views.registrarCita),name="registroCita"),
    path('Cita/editar/<int:id>',login_required(views.editarCita),name="editarCita"),
    path('Cita/anular/<int:id>',login_required(views.anularCita), name="anularCita"),
    path('Consulta', login_required(views.consultaVista),name="consulta"),
    path('Consulta/editar/<int:id>',login_required(views.editarConsulta),name="editarConsulta"),
    path('Consulta/guardar', login_required(views.guardarConsulta), name="guardarConsulta"),
    path('Cuenta',login_required(views.cuentaVista), name="cuenta"),
    path('Cuenta/estado/<int:id>', login_required(views.visualizarCuenta), name="visualizarCuenta"),
    path('ActualizarCuenta',login_required(views.actualizarCuenta), name="actualizarCuenta"),
    path('Cuenta/busqueda', login_required(views.busquedaCuenta), name='busquedaCuenta'),
    path('Reportes/paciente', pdfPaciente, name="reportePaciente")
]