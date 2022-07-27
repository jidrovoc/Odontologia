from django.db import models



# Create your models here.
class historial(models.Model):
    idHistorial=models.AutoField(primary_key=True)
    #idDoctor=models.ForeignKey(doctor, on_delete=models.CASCADE)
    #idTratamiento=models.ForeignKey(tratamiento, ondelete=models.CASCADE)
    tipoSangre=models.CharField(max_length=200)
    correo=models.EmailField(max_length=200)