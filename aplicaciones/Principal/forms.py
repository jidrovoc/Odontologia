from pyexpat import model
from ssl import Options
from django import forms
from .models import *

sexoTipo = ['M', 'F']
class pacienteForm(forms.ModelForm):
    class Meta:
        model=paciente
        fields=[
            'nombres',
            'apellidos',
            'fecNacimiento',
            'sexo',
            'cedula',
            'telefono',
            'correo'
        ]
        widgets={
            'nombres':forms.TextInput(attrs={'Placeholder':'Nombres del Paciente'}),
            'apellidos':forms.TextInput(attrs={'Placeholder':'Apellidos del Paciente'}),
            'fecNacimiento':forms.DateTimeInput(attrs={}),
            'sexo':forms.SelectDateWidget(attrs={'Placeholder':'Nombres del Paciente'}),
            'cedula':forms.TextInput(attrs={'Placeholder':'Cédula del Paciente'}),
            'telefono':forms.TextInput(attrs={'Placeholder':'Teléfono del Paciente'}),
            'correo':forms.TextInput(attrs={'Placeholder':'Correo del Paciente'})
        }