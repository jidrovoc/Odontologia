from datetime import datetime
from multiprocessing.sharedctypes import Value
import string
from time import strftime
from django.db import models


# Create your models here.

class paciente(models.Model):
    idPaciente=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=200)
    apellidos=models.CharField(max_length=200)
    fecNacimiento=models.DateField()
    sexo=models.CharField(max_length=1)
    cedula=models.CharField(max_length=10)
    telefono=models.CharField(max_length=10)
    correo=models.EmailField(max_length=200)


    def __str__(self):
        fila="nombres: "+ self.nombres + " - " + "apellidos: " + self.apellidos + "-" + "fecNacimiento: "+ self.fecNacimiento.strftime('%d/%m/%Y')   + "-" + "sexo: " + self.sexo + "-" + "cedula: " + self.cedula + "-" + "telefono: " + self.telefono + "-" + "correo: " + self.correo
        return fila

    def calcularEdad(self):
        return datetime.today().year-self.fecNacimiento.year

    # def delete(self, using=None, keep_parents=False):
    #     self.imagen.storage.delete(self.imagen.name)
    #     super().delete()