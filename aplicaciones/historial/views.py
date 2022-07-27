from django.shortcuts import render
from .models import historial

# Create your views here.
def inicio(request):
    return render(request, 'base.html')
def historial(request):
    return render(request, 'historial/index.html')
def nuevaHistoria(request):
    return render(request, 'historial/historia.html')