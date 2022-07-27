from ctypes.wintypes import POINT
from datetime import date
from genericpath import exists
from logging import INFO
from operator import concat
from pydoc import doc
from sys import flags
from tkinter import messagebox
from typing import Concatenate
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from tkinter import messagebox as MessageBox
from django.core.paginator import Paginator
from django.db.models import Q, Sum


def inicio(request):
    try:
        return redirect('login')
    except:
        return redirect('login')

        
    

def registroIngreso(id, fecha):
    usuario=ingresoUsuario.objects.create(idUsuario_id=id, fecha=fecha)

# def validarIngreso(request):
#     try:
#         nombre=request.POST['usuario']
#         clave=request.POST['clave']
#         usuarioConsulta=usuario.objects.get(nombre=nombre, clave=clave)
#         if (nombre==usuarioConsulta.nombre and clave==usuarioConsulta.clave):
            
#             return redirect('dashboard')
#         else:
            
#             return redirect(request, '/')
#     except:
        # return redirect('/')
    
def dashboard(request):
    try:
        consultaPaciente=paciente.objects.all().count()
        consultaDoctor=doctor.objects.all().count()
        consultaCita=cita.objects.filter(estado='Pendiente').all().count()
        consultaTratamiento=tratamiento.objects.all().count()
        ca='Pendiente'
        consultaCitaPendiente = cita.objects.filter(estado='Pendiente').order_by('-fecha')[:10]
        consultaCuenta = estadoCuenta.objects.filter(idPaciente__estado=1).order_by('saldo')[:10]
        # consultaCitaPendiente=cita.objects.raw("select top 10 idCita,nombres, fecha from dbo.Principal_cita cita inner join dbo.Principal_paciente paciente on cita.idPaciente_id=paciente.idPaciente where cita.estado='%s' order by fecha desc" %ca)
        # consultaCuenta=estadoCuenta.objects.raw("select top 10 idEstado, nombres, apellidos, fecha, abono, saldo from dbo.Principal_estadocuenta estado inner join dbo.Principal_paciente paciente on estado.idPaciente_id=paciente.idPaciente order by saldo desc")
        return render(request, 'dashboard/index.html',{'consultaPaciente':consultaPaciente,'consultaDoctor':consultaDoctor,'consultaCita':consultaCita,'consultaTratamiento':consultaTratamiento,'consultaCitaPendiente':consultaCitaPendiente,'consultaCuenta':consultaCuenta})
    except:
        return redirect('login')

    

def pacienteVista(request):
    try:
        pacientes = paciente.objects.filter(estado=1).order_by('-idPaciente')
        # pacientes=paciente.objects.raw('select idPaciente, nombres, apellidos,sexo, fecNacimiento, cedula, telefono, correo from dbo.Principal_paciente where estado=1 order by idPaciente desc')
        page=request.GET.get('page',1)
        paginator=Paginator(pacientes, 10)
        pacientes=paginator.page(page)
        return render(request, 'paciente/index.html', {'entity':pacientes, 'paginator':paginator})
    except:
        return redirect('login')
    

def busquedaPaciente(request):
        dato = ''
        pacienteConsulta = None
        if 'buscarPaciente' in request.POST:
            dato =request.POST['buscarPaciente'] 
        if dato != '':
            pacienteConsulta=paciente.objects.filter((Q(nombres__icontains=dato) | Q(apellidos__icontains=dato) | Q(cedula__icontains=dato)) & Q(estado=True))
        else:
            return redirect('paciente')
        return render(request, 'paciente/index.html', {'entity':pacienteConsulta})


def nuevoPaciente(request):
    try:
        return render(request, 'paciente/crear.html')
    except:
        return redirect('login')
    

def registrarPaciente(request):
    try:
        nombre=request.POST['txtNombre']
        apellido=request.POST['txtApellido'] 
        cedula=request.POST['txtCedula']
        fecha=request.POST['txtFecha']
        sexo=request.POST['sexo']
        telefono=request.POST['txtTelefono']
        correo=request.POST['txtCorreo']
        
        if not request.POST['txtId']:
            comparar=paciente.objects.filter(nombres=nombre,apellidos=apellido, estado=True).count()
            compararCedula=paciente.objects.filter(cedula=cedula, estado=True).count()
            if comparar==0 and compararCedula==0:
                pacientes=paciente.objects.create(nombres=nombre, apellidos=apellido,sexo=sexo,cedula=cedula,fecNacimiento=fecha,telefono=telefono,correo=correo, estado=True)
        else:
            id=request.POST['txtId']
            print(id)
            paciente.objects.filter(idPaciente=id).update(nombres=nombre, apellidos=apellido, cedula=cedula, fecNacimiento=fecha, sexo=sexo, telefono=telefono, correo=correo)
            # pacientes=paciente.objects.raw('update dbo.Principal_paciente set nombres=nombre, apellidos=apellido, cedula=cedula, fecNacimiento=fecha, sexo=sexo, telefono=telefono, correo=correo where idPaciente='+ id)
        return redirect('paciente')
    except:
        return redirect('login')
    

def eliminarPaciente(request, id):
    try:
        pacienteEliminar=paciente.objects.filter(idPaciente=id).update(estado=False)
        return redirect('paciente')
    except:
        return redirect('login')
    


def editarPaciente(request, id):
    try:
        pacienteEditar=paciente.objects.get(idPaciente=id)
        fecha = pacienteEditar.fecNacimiento
        fechaPaciente = fecha.strftime("%Y-%m-%d")
        return render(request, 'paciente/editar.html', {'pacienteEditar':pacienteEditar, 'fecha': str(fechaPaciente)})
    except:
        return redirect('login')

# def guardarEdicionPaciente(request):
#     return redirect('/')

def tratamientoVista(request):
    try:
        tratamientoConsulta = tratamiento.objects.filter(estado=1)
        # tratamientoConsulta=tratamiento.objects.raw('select idTratamiento, tratamiento.nombre as Tratamiento, area.nombre as Area, precio from dbo.Principal_tratamiento tratamiento inner join dbo.Principal_areatratamiento area on tratamiento.idArea_id=area.idArea where tratamiento.estado=1')
        page=request.GET.get('page',1)
        paginator=Paginator(tratamientoConsulta, 10)
        tratamientoConsulta=paginator.page(page)
        return render(request, 'tratamiento/index.html', {'entity':tratamientoConsulta,'paginator':paginator})
    except:
        return redirect('login')
    

def busquedaTratamiento(request):
        dato = ''
        table = True
        tratamientoConsulta = None
        if 'buscarTratamiento' in request.POST:
            dato =request.POST['buscarTratamiento'] 
        if dato != '':
            tratamientoConsulta=tratamiento.objects.filter((Q(nombre__icontains=dato) | Q(idArea__nombre__icontains=dato)) & Q(estado=True)).all()
        else:
            return redirect('tratamiento')
        return render(request, 'Tratamiento/index.html', {'entity':tratamientoConsulta, 'tabla':table})


def nuevoTratamiento(request):
    try:
        cargarArea = areaTratamiento.objects.filter(estado=1)
        # cargarArea=areaTratamiento.objects.raw('select idArea, nombre from dbo.Principal_areatratamiento')
        return render(request, 'tratamiento/crear.html', {'cargarArea':cargarArea})
    except:
        return redirect('login')
    

def obtenerIdArea(nombre):
    try:
        consulta = areaTratamiento.objects.filter(nombre=nombre)
        # consulta=areaTratamiento.objects.raw('select * from dbo.Principal_areatratamiento where nombre=%s'% nombre)
        return consulta
    except:
        return redirect('login')
    

def registrarTratamiento(request):
    try:
        nombre=request.POST['txtNombre']
        precio=request.POST['txtPrecio']
        area=request.POST['idArea']
        #areaConsulta=areaTratamiento.objects.raw('select idArea from dbo.Principal_areatratamiento where nombre=%s',[area])[0]
        #areaConsulta=obtenerIdArea(area)
        #idA=areaTratamiento.objects.get(nombre=area)
        #idA=areaTratamiento.objects.raw('select * from dbo.Principal_areatratamiento where nombre=%s', [area])
        if not request.POST['txtId']:
            comparar=tratamiento.objects.filter(nombre=nombre, idArea_id=area, estado=True).count()
            if comparar == 0:
                tratamiento.objects.create(nombre=nombre, precio=precio, idArea_id=area, estado=True)
        else:
            id=request.POST['txtId']
            tratamiento.objects.filter(idTratamiento=id).update(nombre=nombre, precio=precio, idArea_id=area)
        tratamientoConsulta = tratamiento.objects.filter(estado=1)
        # tratamientoConsulta=tratamiento.objects.raw('select idTratamiento, tratamiento.nombre as Tratamiento, area.nombre as Area, precio from dbo.Principal_tratamiento tratamiento inner join dbo.Principal_areatratamiento area on tratamiento.idArea_id=area.idArea')
        return redirect('tratamiento')
    except:
        return redirect('login')
    

def editarTratamiento(request, id):
    try:
        idAreaConsulta=tratamiento.objects.get(idTratamiento=id)
        idA=idAreaConsulta.idArea_id
        nombreAreaConsulta=areaTratamiento.objects.get(idArea=idA)
        nombre=nombreAreaConsulta.nombre
        tratamientoEditar=tratamiento.objects.get(idTratamiento=id)
        areaCargar = areaTratamiento.objects.filter(estado=1)
        # areaCargar=areaTratamiento.objects.raw('select idArea, nombre from dbo.Principal_areatratamiento')
        return render(request, 'tratamiento/editar.html', {'tratamientoEditar':tratamientoEditar,'nombre':nombre,'cargarArea':areaCargar})
    except:
        return redirect('login')
    

def eliminarTratamiento(request, id):
    try:
        tratamiento.objects.filter(idTratamiento=id).update(estado=False)
        return redirect('tratamiento')
    except:
        return redirect('login')
    

def area(request):
    try:
        areaConsulta = areaTratamiento.objects.filter(estado=1).order_by('-idArea')
        # areaConsulta=areaTratamiento.objects.raw('select idArea, nombre from dbo.Principal_areatratamiento where estado=1 order by idArea desc')
        page=request.GET.get('page',1)
        paginator=Paginator(areaConsulta, 5)
        areaConsulta=paginator.page(page)
        return render(request, 'area/index.html', {'entity':areaConsulta,'paginator':paginator})
    except:
        return redirect('login')


def busquedaArea(request):
        dato = ''
        areaConsulta = None
        if 'buscarArea' in request.POST:
            dato =request.POST['buscarArea'] 
        if dato != '':
            areaConsulta=areaTratamiento.objects.filter((Q(nombre__icontains=dato)) & Q(estado=True)).all()
        else:
            return redirect('area')
        return render(request, 'Area/index.html', {'entity':areaConsulta})


def nuevaArea(request):
    try:
        return render(request, 'area/crear.html')
    except:
        return redirect('login')
    
 
def registrarArea(request):
    try:
        nombre=request.POST['txtArea']
        if not request.POST['txtId']:
            comparar=areaTratamiento.objects.filter(nombre=nombre, estado=True).count()
            if comparar == 0:
                area=areaTratamiento.objects.create(nombre=nombre, estado=True)
        else:
            id=request.POST['txtId']
            areaTratamiento.objects.filter(idArea=id).update(nombre=nombre)
            # pacientes=paciente.objects.raw('update dbo.Principal_paciente set nombres=nombre, apellidos=apellido, cedula=cedula, fecNacimiento=fecha, sexo=sexo, telefono=telefono, correo=correo where idPaciente='+ id)
        return redirect('area')
    except:
        return redirect('login')
    

def editarArea(request, id):
    try:
        areaEditar=areaTratamiento.objects.get(idArea=id)
        return render(request, 'area/editar.html', {'areaEditar':areaEditar})
    except:
        return redirect('login')
    

def eliminarArea(request, id):
    try:
        areaEliminar=areaTratamiento.objects.filter(idArea=id).update(estado=False)
        return redirect('area')
    except:
        return redirect('login')
    

def historia(request):
    try:
        historiaConsulta=historial.objects.filter(status=1)
        # historiaConsulta=historial.objects.raw('select historial.idHistorial, paciente.nombres, paciente.apellidos, paciente.fecNacimiento, paciente.cedula from dbo.Principal_historial historial inner join dbo.Principal_paciente paciente on historial.idPaciente_id=paciente.idPaciente where status=1')
        page=request.GET.get('page',1)
        paginator=Paginator(historiaConsulta, 10)
        historiaConsulta=paginator.page(page)
        return render(request, 'historial/index.html', {'entity':historiaConsulta,'paginator':paginator})
    except:
        return redirect('login')
    

def busquedaHistorial(request):
        dato = ''
        historialConsulta = None
        if 'buscarHistorial' in request.POST:
            dato =request.POST['buscarHistorial'] 
        if dato != '':
            historialConsulta=historial.objects.filter((Q(idPaciente__nombres__icontains=dato) | Q(idPaciente__apellidos__icontains=dato) | Q(idPaciente__cedula__icontains=dato)) & Q(status=True))
        else:
            return redirect('historial')
        return render(request, 'historial/index.html', {'entity':historialConsulta})


def nuevaHistoria(request ,id):
        ultimaCita = None
        idPaciente=historial.objects.get(idHistorial=id)
        consultaPaciente=paciente.objects.get(idPaciente=idPaciente.idPaciente_id)
        consultaHistorial=historial.objects.get(idHistorial=id)
        idOdontograma_Historial=historial.objects.filter(idHistorial=id).values()
        intento=historial.objects.filter(idHistorial=id).values_list('idOdontograma')
        idOdonto=odontograma.objects.get(idOdontograma=intento[0][0], estado=True)
        ultimaCita = cita.objects.filter(idPaciente=idPaciente.idPaciente_id).last()
        ultimaConsulta = consulta.objects.filter(idCita=ultimaCita.idCita).values_list('motivo').last()
        idHistoOdonto=None
        fechaPaciente = (consultaPaciente.fecNacimiento).strftime("%Y-%m-%d")
        # hoy = date.today()
        # age = hoy.year - fechaPaciente.year - ((hoy.month, hoy.day) < (fechaPaciente.month, fechaPaciente.day))
        alergias = alergia.objects.filter(idHistorial=id).all()
        page=request.GET.get('page',1)
        paginator=Paginator(alergias, 5)
        alergias=paginator.page(page)
        try:
            idHistoOdonto=odontograma.objects.get(idOdontograma=intento[0][0],estado=False)
        except:
            idHistoOdonto=None
        return render(request, 'historial/historia.html', {'fechaPaciente':fechaPaciente,'consultaPaciente':consultaPaciente, 'consultaHistorial':consultaHistorial, 'colores':idOdonto,'historialOdontogramas':idHistoOdonto,'entity':alergias, 'paginator':paginator, 'ultimaConsulta':ultimaConsulta})
    
    
def alergiaVista(request, id):
    try:
        idPaciente = historial.objects.filter(idHistorial=id,status=True).values_list('idPaciente_id')
        pacienteDato = paciente.objects.filter(idPaciente = idPaciente[0][0]).all()
        alergias = alergia.objects.filter(idHistorial=id).all()
        page=request.GET.get('page',1)
        paginator=Paginator(alergias, 5)
        alergias=paginator.page(page)
        return render(request, 'historial/alergia.html', {'entity':alergias, 'paciente':pacienteDato, 'historial':id, 'paginator':paginator})
    except:
        return redirect('nuevaArea')


def guardarAlergia(request):
    try:
        historial = request.POST['txtHistorial']
        nombre = request.POST['txtNombre']
        observacion = request.POST['txtObservacion']
        aler = alergia.objects.create(idHistorial_id=int(historial), nombre=nombre, observacion=observacion)
        return redirect('alergia',id=historial)
    except:
        return redirect('login')


def actualizar(request):
    try:
        idHistorial = request.GET['idHistorial']
        tiempoEnfermedad = request.GET['tiempoEnfermedad']
        signosPrincipales = request.GET['signosPrincipales']
        antecedentesPersonales = request.GET['antecedentesPersonales']
        pesoPaciente = request.GET['pesoPaciente']
        tallaPaciente = request.GET['tallaPaciente']
        imcPaciente = request.GET['imcPaciente']
        historial.objects.filter(idHistorial=idHistorial).update(tiempoEnfermedad=tiempoEnfermedad,signoPrincipal=signosPrincipales, antecedentesPersonales=antecedentesPersonales, peso=pesoPaciente,talla=tallaPaciente, imc=imcPaciente)
        return JsonResponse({"result":"ok"})
    except:
        return JsonResponse({"result":"bad"})


def diagnosticoVista(request, id, idHistorial):
        pacienteDato = paciente.objects.filter(idPaciente = id).all()
        diagnostico = tratamientoRealizado.objects.filter(idPaciente=id).all()
        page=request.GET.get('page',1)
        paginator=Paginator(diagnostico, 5) 
        diagnostico=paginator.page(page)
        return render(request, 'historial/diagnostico.html', {'entity':diagnostico, 'paginator':paginator, 'historia':idHistorial, 'paciente':pacienteDato})


def tratamientosRealizadosVista(request, id, idHistorial):
        tratamientos = []
        pacienteDato = paciente.objects.filter(idPaciente = id).all()
        if tratamientoRealizado.objects.filter(idPaciente=id).exists():
            tratamientos = tratamientoRealizado.objects.filter(idPaciente=id).all()      
        page=request.GET.get('page',1)
        paginator=Paginator(tratamientos, 5)
        tratamientos=paginator.page(page)
        return render(request, 'historial/tratamiento.html', {'entity':tratamientos,'paginator':paginator,'historia':idHistorial, 'paciente':pacienteDato})


def odontogramaVista(request, id, idHistorial):

        historia = historial.objects.filter(idPaciente_id=id).values_list('idOdontograma')
        odontogramas = odontograma.objects.filter(idOdontograma__in=historia).values_list('idOdontograma', 'estado', 'fecha')
        intento=historial.objects.filter(idHistorial=idHistorial).values_list('idOdontograma')
        idOdonto=odontograma.objects.get(idOdontograma=intento[0][0], estado=True)
        idPaciente = historial.objects.filter(idHistorial=idHistorial,status=True).values_list('idPaciente_id')
        pacienteDato = paciente.objects.filter(idPaciente = idPaciente[0][0]).all()
        page=request.GET.get('page',1)
        paginator=Paginator(odontogramas, 5)
        odontogramas=paginator.page(page)
        return render(request, 'historial/odontograma.html', {'entity':odontogramas, 'paginator':paginator, 'historia':idHistorial, 'paciente':pacienteDato, 'colores':idOdonto})


def visualizarOdontograma(request, id, idHistorial, idOdontogra):
        historia = historial.objects.filter(idPaciente_id=id).values_list('idOdontograma')
        odontogramas = odontograma.objects.filter(idOdontograma__in=historia).values_list('idOdontograma', 'estado', 'fecha')
        idOdonto=odontograma.objects.get(idOdontograma=idOdontogra)
        print(idOdonto)
        idPaciente = historial.objects.filter(idHistorial=idHistorial,status=True).values_list('idPaciente_id')
        pacienteDato = paciente.objects.filter(idPaciente = idPaciente[0][0]).all()
        page=request.GET.get('page',1)
        paginator=Paginator(odontogramas, 5)
        odontogramas=paginator.page(page)
        return render(request, 'historial/odontograma.html', {'entity':odontogramas, 'paginator':paginator, 'historia':idHistorial, 'paciente':pacienteDato, 'colores':idOdonto})


def historialDiagnostico(request, idPaciente, idHistorial):
    try:
        diagnostico = tratamientoRealizado.objects.filter(idPaciente=idPaciente)
        return render(request, 'historial/diagnostico.html',{})
    except:
        return redirect('login')


def doctorVista(request):
    try: 
        doctorConsulta = []
        if 'buscarDoctor' in request.GET:
            print("SI existe")
        else:
            doctorConsulta = doctor.objects.filter(estado=1)
            # doctorConsulta=doctor.objects.raw('select *from dbo.Principal_doctor where estado=1')
        page=request.GET.get('page',1)
        paginator=Paginator(doctorConsulta, 10)
        doctorConsulta=paginator.page(page)
        return render(request, 'doctor/index.html', {'entity':doctorConsulta,'paginator':paginator})
    except:
        return redirect('login')
    
def busquedaDoctor(request):
        dato = ''
        doctorConsulta = None
        if 'buscarDoctor' in request.POST:
            dato =request.POST['buscarDoctor'] 
        if dato != '':
            doctorConsulta=doctor.objects.filter((Q(nombres__icontains=dato) | Q(apellidos__icontains=dato) | Q(cedula__icontains=dato)) & Q(estado=True))
        else:
            return redirect('doctor')
        return render(request, 'doctor/index.html', {'entity':doctorConsulta})


def nuevoDoctor(request):
    try:
        return render(request, 'doctor/crear.html')
    except:
        return redirect('login')
    

def registrarDoctor(request):
    try:
        nombre=request.POST['txtNombre']
        apellido=request.POST['txtApellido']
        cedula=request.POST['txtCedula']
        fecha=request.POST['txtFecha']
        sexo=request.POST['sexo']
        telefono=request.POST['txtTelefono']
        correo=request.POST['txtCorreo']
        especialidad=request.POST['txtEspecialidad']
        
        if not request.POST['txtId']:
            comparar=doctor.objects.filter(nombres=nombre,apellidos=apellido, estado=True).count()
            compararCedula=doctor.objects.filter(cedula=cedula, estado=True).count()
            if comparar==0 and compararCedula==0:
                doctores=doctor.objects.create(nombres=nombre, apellidos=apellido,sexo=sexo,cedula=cedula,fecNacimiento=fecha,telefono=telefono,correo=correo, especialidad=especialidad, estado=True)
        else:
            id=request.POST['txtId']
            doctor.objects.filter(idDoctor=id).update(nombres=nombre, apellidos=apellido, cedula=cedula, fecNacimiento=fecha, sexo=sexo, telefono=telefono, correo=correo, especialidad=especialidad)
            # pacientes=paciente.objects.raw('update dbo.Principal_paciente set nombres=nombre, apellidos=apellido, cedula=cedula, fecNacimiento=fecha, sexo=sexo, telefono=telefono, correo=correo where idPaciente='+ id)
        doctorConsulta=doctor.objects.raw('select *from dbo.Principal_doctor')
        return redirect('doctor')
    except:
        return redirect('login')
    

def editarDoctor(request, id):
    try:
        doctorEditar=doctor.objects.get(idDoctor=id)
        fecha = doctorEditar.fecNacimiento
        fechaPaciente = fecha.strftime("%Y-%m-%d")
        return render(request, 'doctor/editar.html', {'doctorEditar':doctorEditar,'fecha':fechaPaciente})
    except:
        return redirect('login')
    

def eliminarDoctor(request, id):
    try:
        doctorEliminar=doctor.objects.filter(idDoctor=id).update(estado=False)
        return redirect('doctor')
    except:
        return redirect('login')
    

def citaVista(request):
    try:
        tabla = False
        citaConsulta=cita.objects.filter(status=1, idPaciente__estado=1)
        # citaConsulta=cita.objects.raw('select cita.idCita, paciente.nombres as NombrePaciente, paciente.apellidos as ApellidoPaciente, doctor.nombres as NombreDoctor, doctor.apellidos as ApellidoDoctor, cita.fecha, cita.hora, cita.estado from dbo.Principal_cita cita inner join dbo.Principal_paciente paciente on cita.idPaciente_id=paciente.idPaciente inner join dbo.Principal_doctor doctor on doctor.idDoctor=cita.idDoctor_id where status=1 and paciente.estado=1 order by fecha desc')
        page=request.GET.get('page',1)
        paginator=Paginator(citaConsulta, 10)
        citaConsulta=paginator.page(page)
        return render(request, 'cita/index.html', {'entity':citaConsulta,'paginator':paginator,'tabla':tabla})
    except:
        return redirect('login')
    

def busquedaCita(request):
        citaConsulta = ''
        dato = ''
        if 'buscarCita' in request.POST:
            dato =request.POST['buscarCita'] 
        if dato != '':
            citaConsulta=cita.objects.filter((Q(idPaciente__nombres__icontains=dato) | Q(idPaciente__apellidos__icontains=dato) | Q(idPaciente__cedula__icontains=dato)) & (Q(status=True) & Q(idPaciente__estado=True) )).all()
            tabla = True
        else:
            return redirect('cita')
        return render(request, 'Cita/index.html', {'entity':citaConsulta, 'tabla':tabla})



def nuevaCita(request):
    try:
        cargarPaciente=paciente.objects.filter(estado=1)
        cargarDoctor=doctor.objects.filter(estado=1)
        # cargarPaciente=paciente.objects.raw('select idPaciente, nombres, apellidos from dbo.Principal_paciente where estado=1')
        # cargarDoctor=doctor.objects.raw('select idDoctor, nombres, apellidos from dbo.Principal_doctor where estado=1')
        return render(request, 'cita/crear.html',{'cargarPaciente':cargarPaciente, 'cargarDoctor':cargarDoctor})
    except:
        return redirect('login')
    

def registrarCita(request):
    try:
        paciente=request.POST['idPaciente']
        doctor=request.POST['idDoctor']
        fecha=request.POST['fechaCita']
        hora=request.POST['horaCita']
        descripcion=request.POST['descripcionCita']
        if len(request.POST['txtId']) == 0:
            citaRegistro=cita.objects.create(fecha=fecha, hora=hora, estado='Pendiente', idPaciente_id=paciente, idDoctor_id=doctor,descripcion=descripcion, status=True)
        else:
            id=request.POST['txtId']
            citaRegistro=cita.objects.filter(idCita=id).update(fecha=fecha, hora=hora, estado='Pendiente', idPaciente_id=paciente, idDoctor_id=doctor,descripcion=descripcion)
        #     doctor.objects.filter(idDoctor=id).update(nombres=nombre, apellidos=apellido, cedula=cedula, fecNacimiento=fecha, sexo=sexo, telefono=telefono, correo=correo, especialidad=especialidad)
        #     # pacientes=paciente.objects.raw('update dbo.Principal_paciente set nombres=nombre, apellidos=apellido, cedula=cedula, fecNacimiento=fecha, sexo=sexo, telefono=telefono, correo=correo where idPaciente='+ id)
        return redirect('cita')
    except:
        return redirect('login')
    

def editarCita(request, id):
    try:
        consultaCita=cita.objects.get(idCita=id)
        if consultaCita.estado=='Pendiente':
            idPaciente=consultaCita.idPaciente_id
            idDoctor=consultaCita.idDoctor_id
            datoPaciente=paciente.objects.get(idPaciente=idPaciente)
            datoDoctor=doctor.objects.get(idDoctor=idDoctor)
            cargarPaciente=paciente.objects.filter(estado=1)
            cargarDoctor=doctor.objects.filter(estado=1)
            # cargarPaciente=paciente.objects.raw('select idPaciente, nombres, apellidos from dbo.Principal_paciente')
            # cargarDoctor=doctor.objects.raw('select idDoctor, nombres, apellidos from dbo.Principal_doctor')
            fecha = consultaCita.fecha
            fechaCita = fecha.strftime("%Y-%m-%d")
            hora = (consultaCita.hora).strftime("%H:%M")
            return render(request, 'cita/editar.html', {'consultaCita':consultaCita,'datoPaciente':datoPaciente,'datoDoctor':datoDoctor,'cargarPaciente':cargarPaciente,'cargarDoctor':cargarDoctor, 'fecha':fechaCita,'hora':hora, 'idCita':id})
        return redirect('cita')
    except:
        return redirect('login')
    

def anularCita(request, id):
    try:
        consultaCita=cita.objects.get(idCita=id)
        if consultaCita.estado=='Pendiente':
            idCita=cita.objects.filter(idCita=id).update(estado='Anulado')    
        return redirect('cita')
    except:
        return redirect('login')
    

def consultaVista(request):
    try:
        return render(request, 'consulta/index.html')
    except:
        return redirect('login')
    

def editarConsulta(request, id):
    try:
        idPersona=cita.objects.get(idCita=id)
        if idPersona.estado=='Pendiente':
            consultaPaciente=paciente.objects.get(idPaciente=idPersona.idPaciente_id)
            consultaDoctor=doctor.objects.get(idDoctor=idPersona.idDoctor_id)
            cargarTratamiento=tratamiento.objects.filter(estado=1)
            # cargarTratamiento=tratamiento.objects.raw('select idTratamiento, nombre, precio from dbo.Principal_tratamiento')
            return render(request, 'consulta/editar.html',{'consultaPaciente':consultaPaciente,'consultaDoctor':consultaDoctor,'cita':idPersona.idCita,'cargarTratamiento':cargarTratamiento})
        return redirect('cita')
    except:
        return redirect('login')
    

def guardarConsulta(request):

        idCitas=request.POST['txtCita']
        idPaciente=request.POST['txtIdPaciente'] 
        idDoctor=request.POST['txtIdDoctor']
        motivoConsulta=request.POST['txtMotivoConsulta']
        descripcionProblema=request.POST['txtDescripcionProblema']
        temperatura=request.POST['txtTemperatura'] 
        respiracion=request.POST['txtRespiracion']
        presionArterial=request.POST['txtPresionArterial']
        pulso=request.POST['txtPulso']
        frecuenciaCardiaca=request.POST['txtFrecuenciaCardiaca']
        frecuenciaRespiratoria=request.POST['txtFrecuenciaRespiratoria']
        diagnostico=request.POST['txtDiagnostico']
        diagnosticoObservacion=request.POST['txtDiagnosticoObservacion']
        tratamientoConclusion=request.POST['txtTratamientoConclusion'] 
        abono=request.POST['txtAbonoValor']
        saldo=request.POST['txtSaldoValor']
        idVerificarOdontograma=request.POST['odontoVerificador']
        idOdonto=None
        if (abono != '' and saldo != ''):
            if (float(abono) <= float(saldo) and float(abono) >= 0):
                saldoTotal=float(saldo)-float(abono)
                if (saldo != 0):
                    if (abono <= saldo):
                        saldo = saldo - abono
                    estadoCuenta.objects.create(idPaciente=paciente.objects.get(idPaciente=idPaciente), fecha=date.today(), abono=abono, saldo=saldoTotal)

         
        lista=request.POST.getlist('idTratamientoSelect[]') 
        conclu=request.POST.getlist('txtConclusion[]')
        tamano=len(lista) 
        contador=0
        if (len(lista)>0):
            while contador<tamano:
                tratamientoTemporal.objects.create(idPaciente_id=idPaciente, idTratamiento_id=lista[contador], resumen=conclu[contador], diagnostico=diagnostico, observacionDiagnostico=diagnosticoObservacion)
                contador=contador+1
        else:
            if (len(diagnostico)>0):
                tratamientoTemporal.objects.create(idPaciente_id=idPaciente, diagnostico=diagnostico, observacionDiagnostico=diagnosticoObservacion)
        
        colores=request.POST.getlist('color[]')
        partes=request.POST.getlist('identificador[]')
        verificar=historial.objects.filter(idPaciente__idPaciente=idPaciente).values_list('idOdontograma')
        if verificar:
            odontograma.objects.filter(idOdontograma=verificar[0][0]).update(estado=False)

        consulta.objects.create(motivo=motivoConsulta, descripcion=descripcionProblema, idCita_id=idCitas, temperatura=temperatura, respiracion=respiracion, presionArterial=presionArterial, pulso=pulso, frecuenciaCardiaca=frecuenciaCardiaca, frecuenciaRespiratoria=frecuenciaRespiratoria)
        cita.objects.filter(idCita=idCitas).update(estado='Atendido')

        historialDuplicado = historial.objects.filter(idPaciente=paciente.objects.get(idPaciente=idPaciente),status=True).exists()
        if historialDuplicado:
            if idVerificarOdontograma == '2':
                odonto=odontograma.objects.create(fecha=datetime.today(),TP18=colores[0], BP18=colores[1], RP18=colores[2], LP18=colores[3], CP18=colores[4], CP17=colores[5], TP17=colores[6], BP17=colores[7], RP17=colores[8], LP17=colores[9], CP16=colores[10], TP16=colores[11], BP16=colores[12], RP16=colores[13], LP16=colores[14], CP15=colores[15], TP15=colores[16], BP15=colores[17], RP15=colores[18], LP15=colores[19], CP14=colores[20], TP14=colores[21], BP14=colores[22], RP14=colores[23], LP14=colores[24], CP13=colores[25], TP13=colores[26], BP13=colores[27], RP13=colores[28], LP13=colores[29], CP12=colores[30], TP12=colores[31], BP12=colores[32], RP12=colores[33], LP12=colores[34], CP11=colores[35], TP11=colores[36], BP11=colores[37], RP11=colores[38], LP11=colores[39], CP55=colores[40], TP55=colores[41], BP55=colores[42], RP55=colores[43], LP55=colores[44], CP54=colores[45], TP54=colores[46], BP54=colores[47], RP54=colores[48], LP54=colores[49], CP53=colores[50], TP53=colores[51], BP53=colores[52], RP53=colores[53], LP53=colores[54], CP52=colores[55], TP52=colores[56], BP52=colores[57], RP52=colores[58], LP52=colores[59], CP51=colores[60], TP51=colores[61], BP51=colores[62], RP51=colores[63], LP51=colores[64], CP85=colores[65], TP85=colores[66], BP85=colores[67], RP85=colores[68], LP85=colores[69], CP84=colores[70], TP84=colores[71], BP84=colores[72], RP84=colores[73], LP84=colores[74], CP83=colores[75], TP83=colores[76], BP83=colores[77], RP83=colores[78], LP83=colores[79], CP82=colores[80], TP82=colores[81], BP82=colores[82], RP82=colores[83], LP82=colores[84], CP81=colores[85], TP81=colores[86], BP81=colores[87], RP81=colores[88], LP81=colores[89], CP48=colores[90], TP48=colores[91], BP48=colores[92], RP48=colores[93], LP48=colores[94], CP47=colores[95], TP47=colores[96], BP47=colores[97], RP47=colores[98], LP47=colores[99], CP46=colores[100], TP46=colores[101], BP46=colores[102], RP46=colores[103], LP46=colores[104], CP45=colores[105], TP45=colores[106], BP45=colores[107], RP45=colores[108], LP45=colores[109], CP44=colores[110], TP44=colores[111], BP44=colores[112], RP44=colores[113], LP44=colores[114], CP43=colores[115], TP43=colores[116], BP43=colores[117], RP43=colores[118], LP43=colores[119], CP42=colores[120], TP42=colores[121], BP42=colores[122], RP42=colores[123], LP42=colores[124], CP41=colores[125], TP41=colores[126], BP41=colores[127], RP41=colores[128], LP41=colores[129], CP21=colores[130], TP21=colores[131], BP21=colores[132], RP21=colores[133], LP21=colores[134], CP22=colores[135], TP22=colores[136], BP22=colores[137], RP22=colores[138], LP22=colores[139], CP23=colores[140], TP23=colores[141], BP23=colores[142], RP23=colores[143], LP23=colores[144], CP24=colores[145], TP24=colores[146], BP24=colores[147], RP24=colores[148], LP24=colores[149], CP25=colores[150], TP25=colores[151], BP25=colores[152], RP25=colores[153], LP25=colores[154], CP26=colores[155], TP26=colores[156], BP26=colores[157], RP26=colores[158], LP26=colores[159], CP27=colores[160], TP27=colores[161], BP27=colores[162], RP27=colores[163], LP27=colores[164], CP28=colores[165], TP28=colores[166], BP28=colores[167], RP28=colores[168], LP28=colores[169], CP61=colores[170], TP61=colores[171], BP61=colores[172], RP61=colores[173], LP61=colores[174], CP62=colores[175], TP62=colores[176], BP62=colores[177], RP62=colores[178], LP62=colores[179], CP63=colores[180], TP63=colores[181], BP63=colores[182], RP63=colores[183], LP63=colores[184], CP64=colores[185], TP64=colores[186], BP64=colores[187], RP64=colores[188], LP64=colores[189], CP65=colores[190], TP65=colores[191], BP65=colores[192], RP65=colores[193], LP65=colores[194], CP71=colores[195], TP71=colores[196], BP71=colores[197], RP71=colores[198], LP71=colores[199], CP72=colores[200], TP72=colores[201], BP72=colores[202], RP72=colores[203], LP72=colores[204], CP73=colores[205], TP73=colores[206], BP73=colores[207], RP73=colores[208], LP73=colores[209], CP74=colores[210], TP74=colores[211], BP74=colores[212], RP74=colores[213], LP74=colores[214], CP75=colores[215], TP75=colores[216], BP75=colores[217], RP75=colores[218], LP75=colores[219], CP31=colores[220], TP31=colores[221], BP31=colores[222], RP31=colores[223], LP31=colores[224], CP32=colores[225], TP32=colores[226], BP32=colores[227], RP32=colores[228], LP32=colores[229], CP33=colores[230], TP33=colores[231], BP33=colores[232], RP33=colores[233], LP33=colores[234], CP34=colores[235], TP34=colores[236], BP34=colores[237], RP34=colores[238], LP34=colores[239], CP35=colores[240], TP35=colores[241], BP35=colores[242], RP35=colores[243], LP35=colores[244], CP36=colores[245], TP36=colores[246], BP36=colores[247], RP36=colores[248], LP36=colores[249], CP37=colores[250], TP37=colores[251], BP37=colores[252], RP37=colores[253], LP37=colores[254], CP38=colores[255], TP38=colores[256], BP38=colores[257], RP38=colores[258], LP38=colores[259], estado=True)
                idOdonto=odontograma.objects.get(idOdontograma=odonto.idOdontograma)
                id=historial.objects.filter(idPaciente=paciente.objects.get(idPaciente=idPaciente),status=True).values_list('idHistorial')
                historial.objects.filter(idHistorial=id[0][0]).update(status=False)
                rh = historial.objects.get(idHistorial=id)
                historial.objects.create(idPaciente=rh.idPaciente, idOdontograma=rh.idOdontograma, tiempoEnfermedad=rh.tiempoEnfermedad, motivoConsulta=rh.motivoConsulta, signoPrincipal=rh.signoPrincipal, antecedentesPersonales=rh.antecedentesPersonales, descripcionTratamientoOrtodoncia=rh.descripcionTratamientoOrtodoncia, tratamientoOrtodoncia=rh.tratamientoOrtodoncia, medicamento=rh.medicamento, descripcionMedicamento=rh.descripcionMedicamento, descripcionAlergia=rh.descripcionAlergia, alergiaMedicamento=rh.alergiaMedicamento, trastornoNervioso=rh.trastornoNervioso,descripcionTrastorno=rh.descripcionTrastorno, antecedentePersonal=rh.antecedentePersonal, imc=rh.imc, peso=rh.peso, presionArterial=rh.presionArterial,pulso=rh.pulso, respiracion=rh.respiracion, talla=rh.talla, temperatura=rh.temperatura, frecuenciaRespiratoria=rh.frecuenciaRespiratoria, frecuenciaCardiaca=rh.frecuenciaCardiaca)
                # historial.objects.raw("Insert Into Principal_historial (idPaciente_id, idOdontograma_id, tiempoEnfermedad, motivoConsulta,signoPrincipal, antecedentesPersonales, descripcionTratamientoOrtodoncia, tratamientoOrtodoncia,medicamento, descripcionMedicamento, descripcionAlergia, alergiaMedicamento, trastornoNervioso,descripcionTrastorno, antecedentePersonal, imc, peso, presionArterial,pulso, respiracion, talla, temperatura, frecuenciaRespiratoria, frecuenciaCardiaca) select idPaciente_id, idOdontograma_id, tiempoEnfermedad, motivoConsulta,signoPrincipal, antecedentesPersonales, descripcionTratamientoOrtodoncia, tratamientoOrtodoncia,medicamento, descripcionMedicamento, descripcionAlergia, alergiaMedicamento, trastornoNervioso,descripcionTrastorno, antecedentePersonal, imc, peso, presionArterial,pulso, respiracion, talla, temperatura, frecuenciaRespiratoria, frecuenciaCardiaca From Principal_historial Where idHistorial = '%s'" %id)
                idNuevoHistorial = historial.objects.filter(idPaciente=idPaciente).last()
                print(idNuevoHistorial.idHistorial)
                historial.objects.filter(idHistorial=idNuevoHistorial.idHistorial).update(status=True, idOdontograma=idOdonto)
        else:
                odonto=odontograma.objects.create(fecha=datetime.today(),TP18=colores[0], BP18=colores[1], RP18=colores[2], LP18=colores[3], CP18=colores[4], CP17=colores[5], TP17=colores[6], BP17=colores[7], RP17=colores[8], LP17=colores[9], CP16=colores[10], TP16=colores[11], BP16=colores[12], RP16=colores[13], LP16=colores[14], CP15=colores[15], TP15=colores[16], BP15=colores[17], RP15=colores[18], LP15=colores[19], CP14=colores[20], TP14=colores[21], BP14=colores[22], RP14=colores[23], LP14=colores[24], CP13=colores[25], TP13=colores[26], BP13=colores[27], RP13=colores[28], LP13=colores[29], CP12=colores[30], TP12=colores[31], BP12=colores[32], RP12=colores[33], LP12=colores[34], CP11=colores[35], TP11=colores[36], BP11=colores[37], RP11=colores[38], LP11=colores[39], CP55=colores[40], TP55=colores[41], BP55=colores[42], RP55=colores[43], LP55=colores[44], CP54=colores[45], TP54=colores[46], BP54=colores[47], RP54=colores[48], LP54=colores[49], CP53=colores[50], TP53=colores[51], BP53=colores[52], RP53=colores[53], LP53=colores[54], CP52=colores[55], TP52=colores[56], BP52=colores[57], RP52=colores[58], LP52=colores[59], CP51=colores[60], TP51=colores[61], BP51=colores[62], RP51=colores[63], LP51=colores[64], CP85=colores[65], TP85=colores[66], BP85=colores[67], RP85=colores[68], LP85=colores[69], CP84=colores[70], TP84=colores[71], BP84=colores[72], RP84=colores[73], LP84=colores[74], CP83=colores[75], TP83=colores[76], BP83=colores[77], RP83=colores[78], LP83=colores[79], CP82=colores[80], TP82=colores[81], BP82=colores[82], RP82=colores[83], LP82=colores[84], CP81=colores[85], TP81=colores[86], BP81=colores[87], RP81=colores[88], LP81=colores[89], CP48=colores[90], TP48=colores[91], BP48=colores[92], RP48=colores[93], LP48=colores[94], CP47=colores[95], TP47=colores[96], BP47=colores[97], RP47=colores[98], LP47=colores[99], CP46=colores[100], TP46=colores[101], BP46=colores[102], RP46=colores[103], LP46=colores[104], CP45=colores[105], TP45=colores[106], BP45=colores[107], RP45=colores[108], LP45=colores[109], CP44=colores[110], TP44=colores[111], BP44=colores[112], RP44=colores[113], LP44=colores[114], CP43=colores[115], TP43=colores[116], BP43=colores[117], RP43=colores[118], LP43=colores[119], CP42=colores[120], TP42=colores[121], BP42=colores[122], RP42=colores[123], LP42=colores[124], CP41=colores[125], TP41=colores[126], BP41=colores[127], RP41=colores[128], LP41=colores[129], CP21=colores[130], TP21=colores[131], BP21=colores[132], RP21=colores[133], LP21=colores[134], CP22=colores[135], TP22=colores[136], BP22=colores[137], RP22=colores[138], LP22=colores[139], CP23=colores[140], TP23=colores[141], BP23=colores[142], RP23=colores[143], LP23=colores[144], CP24=colores[145], TP24=colores[146], BP24=colores[147], RP24=colores[148], LP24=colores[149], CP25=colores[150], TP25=colores[151], BP25=colores[152], RP25=colores[153], LP25=colores[154], CP26=colores[155], TP26=colores[156], BP26=colores[157], RP26=colores[158], LP26=colores[159], CP27=colores[160], TP27=colores[161], BP27=colores[162], RP27=colores[163], LP27=colores[164], CP28=colores[165], TP28=colores[166], BP28=colores[167], RP28=colores[168], LP28=colores[169], CP61=colores[170], TP61=colores[171], BP61=colores[172], RP61=colores[173], LP61=colores[174], CP62=colores[175], TP62=colores[176], BP62=colores[177], RP62=colores[178], LP62=colores[179], CP63=colores[180], TP63=colores[181], BP63=colores[182], RP63=colores[183], LP63=colores[184], CP64=colores[185], TP64=colores[186], BP64=colores[187], RP64=colores[188], LP64=colores[189], CP65=colores[190], TP65=colores[191], BP65=colores[192], RP65=colores[193], LP65=colores[194], CP71=colores[195], TP71=colores[196], BP71=colores[197], RP71=colores[198], LP71=colores[199], CP72=colores[200], TP72=colores[201], BP72=colores[202], RP72=colores[203], LP72=colores[204], CP73=colores[205], TP73=colores[206], BP73=colores[207], RP73=colores[208], LP73=colores[209], CP74=colores[210], TP74=colores[211], BP74=colores[212], RP74=colores[213], LP74=colores[214], CP75=colores[215], TP75=colores[216], BP75=colores[217], RP75=colores[218], LP75=colores[219], CP31=colores[220], TP31=colores[221], BP31=colores[222], RP31=colores[223], LP31=colores[224], CP32=colores[225], TP32=colores[226], BP32=colores[227], RP32=colores[228], LP32=colores[229], CP33=colores[230], TP33=colores[231], BP33=colores[232], RP33=colores[233], LP33=colores[234], CP34=colores[235], TP34=colores[236], BP34=colores[237], RP34=colores[238], LP34=colores[239], CP35=colores[240], TP35=colores[241], BP35=colores[242], RP35=colores[243], LP35=colores[244], CP36=colores[245], TP36=colores[246], BP36=colores[247], RP36=colores[248], LP36=colores[249], CP37=colores[250], TP37=colores[251], BP37=colores[252], RP37=colores[253], LP37=colores[254], CP38=colores[255], TP38=colores[256], BP38=colores[257], RP38=colores[258], LP38=colores[259], estado=True)
                idOdonto=odontograma.objects.get(idOdontograma=odonto.idOdontograma)       
                historial.objects.create(idDoctor=doctor.objects.get(idDoctor=idDoctor), idPaciente=paciente.objects.get(idPaciente=idPaciente), idOdontograma=idOdonto, temperatura=temperatura, respiracion=respiracion, presionArterial=presionArterial, pulso=pulso, frecuenciaCardiaca=frecuenciaCardiaca, frecuenciaRespiratoria=frecuenciaRespiratoria, status=True)
        
       
        return redirect('cita')
 
  
    

def cuentaVista(request):
    try:
        consultaCuenta=estadoCuenta.objects.filter(idPaciente__estado=True)
        page=request.GET.get('page',1)
        paginator=Paginator(consultaCuenta, 10)
        consultaCuenta=paginator.page(page)
        return render(request, 'cuenta/index.html',{'entity':consultaCuenta, 'paginator':paginator})
    except:
        return redirect('login')

def busquedaCuenta(request):
        dato = ''
        cuentaConsulta = None
        if 'buscarCuenta' in request.POST:
            dato =request.POST['buscarCuenta'] 
        if dato != '':
            cuentaConsulta=estadoCuenta.objects.filter((Q(idPaciente__nombres__icontains=dato) | Q(idPaciente__apellidos__icontains=dato) | Q(idPaciente__cedula__icontains=dato)) & Q(idPaciente__estado=True))
        else:
            return redirect('cuenta')
        return render(request, 'cuenta/index.html', {'entity':cuentaConsulta})


def visualizarCuenta(request, id):
    print(id)
    cuenta = estadoCuenta.objects.get(idEstado=id)
    return render(request, 'cuenta/visualizar.html', {'cuenta':cuenta})

def actualizarCuenta(request):
    cancela = request.POST['txtCancela']
    saldo = request.POST['txtSaldo']
    abono = request.POST['txtAbono']
    totalAbono = float(abono) + float(cancela)
    total = float(saldo) - float(cancela)
    cuenta =  estadoCuenta.objects.filter(idEstado=id).update(saldo=total, abono=totalAbono)
    return redirect('cuenta')
def pdfPaciente(request):
    consultaPaciente=paciente.objects.all().order_by('idPaciente')
    return render(request, 'reportes/paciente.html',{'pacientes':consultaPaciente})