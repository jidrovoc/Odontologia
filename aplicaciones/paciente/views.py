from django.shortcuts import render
from .models import paciente
from django.http import HttpResponse
from .models import paciente

# Create your views here.
# def inicio(request):
#     return render(request,'index.html')

def inicio(request):
    return render(request, 'base.html')

def pacienteVista(request):
    pacientes=paciente.objects.all()
    return render(request, 'paciente/index.html', {'pacientes':pacientes})

def nosotros(request):
    return render(request, 'paciente/index.html')

def nuevoPaciente(request):
    return render(request, 'paciente/crear.html')

def editarPaciente(request):
    return render(request, 'paciente/editar.html')
