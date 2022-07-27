from django.shortcuts import render
from .models import areaTratamiento, tratamiento
from django.http import HttpResponse

# Create your views here.
# def inicio(request):
#     return render(request,'index.html')

def inicio(request):
    return render(request, 'base.html')

def tratamientoVista(request):
    tratamientoConsulta=tratamiento.objects.raw('select idTratamiento, tratamiento.nombre as Tratamiento, area.nombre as Area, precio from dbo.tratamiento_tratamiento tratamiento inner join dbo.tratamiento_areatratamiento area on tratamiento.idArea_id=area.idArea')
    #tratamientoConsulta=tratamiento.objects.all()
    return render(request, 'tratamiento/index.html', {'tratamientoConsulta':tratamientoConsulta})

def nuevoTratamiento(request):
    return render(request, 'tratamiento/crear.html')

def editarTratamiento(request):
    return render(request, 'tratamiento/editar.html')

def area(request):
    areaConsulta=areaTratamiento.objects.all()
    return render(request, 'area/index.html', {'areaConsulta':areaConsulta})

def nuevaArea(request):
    return render(request, 'area/crear.html')
