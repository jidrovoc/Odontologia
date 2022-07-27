from django.db import models

# Create your models here.

class areaTratamiento(models.Model):
    idArea=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)

    def __str__(self):
        fila="nombre: " + self.nombre 
        return fila



class tratamiento(models.Model):
    idTratamiento=models.AutoField(primary_key=True)
    idArea=models.ForeignKey(areaTratamiento, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    precio=models.FloatField(max_length=200)

    def __str__(self):
        fila="nombre: " + self.nombre + "-" + "idArea: " + self.idArea + "-" + "precio: " + self.precio
        return fila

   
    