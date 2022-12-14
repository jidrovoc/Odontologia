from datetime import datetime
from multiprocessing.sharedctypes import Value
import string
from time import strftime
from django.db import models

class paciente(models.Model):
    idPaciente=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=200)
    apellidos=models.CharField(max_length=200, verbose_name="Apellidos")
    fecNacimiento=models.DateField(verbose_name="Fecha Nacimiento")
    sexo=models.CharField(max_length=1, verbose_name="Sexo")
    cedula=models.CharField(max_length=10, verbose_name="Cédula")
    telefono=models.CharField(max_length=10, verbose_name="Teléfono")
    correo=models.EmailField(max_length=250, verbose_name="Correo")
    estadoCivil = models.CharField(max_length=150, null=True)
    estado=models.BooleanField(blank=True, null=True)


    def __str__(self):
        fila="nombres: "+ self.nombres + " - " + "apellidos: " + self.apellidos + "-" + "fecNacimiento: "+ self.fecNacimiento.strftime('%d/%m/%Y')   + "-" + "sexo: " + self.sexo + "-" + "cedula: " + self.cedula + "-" + "telefono: " + self.telefono + "-" + "correo: " + self.correo
        return fila

    def calcularEdad(self):
        return datetime.today().year-self.fecNacimiento.year

    # def delete(self, using=None, keep_parents=False):
    #     self.imagen.storage.delete(self.imagen.name)
    #     super().delete()

class doctor(models.Model):
    idDoctor=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=200)
    apellidos=models.CharField(max_length=200)
    fecNacimiento=models.DateField()
    sexo=models.CharField(max_length=1)
    cedula=models.CharField(max_length=10)
    telefono=models.CharField(max_length=10)
    correo=models.EmailField(max_length=250)
    especialidad=models.CharField(max_length=150)
    estado=models.BooleanField(blank=True, null=True)

class areaTratamiento(models.Model):
    idArea=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    estado = models.BooleanField(blank=True, null=True)
    def __str__(self):
        fila="nombre: " + self.nombre 
        return fila



class tratamiento(models.Model):
    idTratamiento=models.AutoField(primary_key=True)
    idArea=models.ForeignKey(areaTratamiento, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    precio=models.FloatField(max_length=200)
    estado = models.BooleanField(blank=True, null=True)
    def __str__(self):
        fila="nombre: " + self.nombre + "-" + "idArea: " + self.idArea + "-" + "precio: " + self.precio
        return fila

class odontograma(models.Model):
    idOdontograma=models.AutoField(primary_key=True)
    fecha=models.DateField(null=True)
    TP18=models.CharField(max_length=50, null=True)
    BP18=models.CharField(max_length=50, null=True)
    RP18=models.CharField(max_length=50, null=True)
    LP18=models.CharField(max_length=50, null=True)
    CP18=models.CharField(max_length=50, null=True)
    CP17=models.CharField(max_length=50, null=True)
    TP17=models.CharField(max_length=50, null=True)
    BP17=models.CharField(max_length=50, null=True)
    RP17=models.CharField(max_length=50, null=True)
    LP17=models.CharField(max_length=50, null=True)
    CP16=models.CharField(max_length=50, null=True)
    TP16=models.CharField(max_length=50, null=True)
    BP16=models.CharField(max_length=50, null=True)
    RP16=models.CharField(max_length=50, null=True)
    LP16=models.CharField(max_length=50, null=True)
    CP15=models.CharField(max_length=50, null=True)
    TP15=models.CharField(max_length=50, null=True)
    BP15=models.CharField(max_length=50, null=True)
    RP15=models.CharField(max_length=50, null=True)
    LP15=models.CharField(max_length=50, null=True)
    CP14=models.CharField(max_length=50, null=True)
    TP14=models.CharField(max_length=50, null=True)
    BP14=models.CharField(max_length=50, null=True)
    RP14=models.CharField(max_length=50, null=True)
    LP14=models.CharField(max_length=50, null=True)
    CP13=models.CharField(max_length=50, null=True)
    TP13=models.CharField(max_length=50, null=True)
    BP13=models.CharField(max_length=50, null=True)
    RP13=models.CharField(max_length=50, null=True)
    LP13=models.CharField(max_length=50, null=True)
    CP12=models.CharField(max_length=50, null=True)
    TP12=models.CharField(max_length=50, null=True)
    BP12=models.CharField(max_length=50, null=True)
    RP12=models.CharField(max_length=50, null=True)
    LP12=models.CharField(max_length=50, null=True)
    CP11=models.CharField(max_length=50, null=True)
    TP11=models.CharField(max_length=50, null=True)
    BP11=models.CharField(max_length=50, null=True)
    RP11=models.CharField(max_length=50, null=True)
    LP11=models.CharField(max_length=50, null=True)
    CP55=models.CharField(max_length=50, null=True)
    TP55=models.CharField(max_length=50, null=True)
    BP55=models.CharField(max_length=50, null=True)
    RP55=models.CharField(max_length=50, null=True)
    LP55=models.CharField(max_length=50, null=True)
    CP54=models.CharField(max_length=50, null=True)
    TP54=models.CharField(max_length=50, null=True)
    BP54=models.CharField(max_length=50, null=True)
    RP54=models.CharField(max_length=50, null=True)
    LP54=models.CharField(max_length=50, null=True)
    CP53=models.CharField(max_length=50, null=True)
    TP53=models.CharField(max_length=50, null=True)
    BP53=models.CharField(max_length=50, null=True)
    RP53=models.CharField(max_length=50, null=True)
    LP53=models.CharField(max_length=50, null=True)
    CP52=models.CharField(max_length=50, null=True)
    TP52=models.CharField(max_length=50, null=True)
    BP52=models.CharField(max_length=50, null=True)
    RP52=models.CharField(max_length=50, null=True)
    LP52=models.CharField(max_length=50, null=True)
    CP51=models.CharField(max_length=50, null=True)
    TP51=models.CharField(max_length=50, null=True)
    BP51=models.CharField(max_length=50, null=True)
    RP51=models.CharField(max_length=50, null=True)
    LP51=models.CharField(max_length=50, null=True)
    CP85=models.CharField(max_length=50, null=True)
    TP85=models.CharField(max_length=50, null=True)
    BP85=models.CharField(max_length=50, null=True)
    RP85=models.CharField(max_length=50, null=True)
    LP85=models.CharField(max_length=50, null=True)
    CP84=models.CharField(max_length=50, null=True)
    TP84=models.CharField(max_length=50, null=True)
    BP84=models.CharField(max_length=50, null=True)
    RP84=models.CharField(max_length=50, null=True)
    LP84=models.CharField(max_length=50, null=True)
    CP83=models.CharField(max_length=50, null=True)
    TP83=models.CharField(max_length=50, null=True)
    BP83=models.CharField(max_length=50, null=True)
    RP83=models.CharField(max_length=50, null=True)
    LP83=models.CharField(max_length=50, null=True)
    CP82=models.CharField(max_length=50, null=True)
    TP82=models.CharField(max_length=50, null=True)
    BP82=models.CharField(max_length=50, null=True)
    RP82=models.CharField(max_length=50, null=True)
    LP82=models.CharField(max_length=50, null=True)
    CP81=models.CharField(max_length=50, null=True)
    TP81=models.CharField(max_length=50, null=True)
    BP81=models.CharField(max_length=50, null=True)
    RP81=models.CharField(max_length=50, null=True)
    LP81=models.CharField(max_length=50, null=True)
    CP48=models.CharField(max_length=50, null=True)
    TP48=models.CharField(max_length=50, null=True)
    BP48=models.CharField(max_length=50, null=True)
    RP48=models.CharField(max_length=50, null=True)
    LP48=models.CharField(max_length=50, null=True)
    CP47=models.CharField(max_length=50, null=True)
    TP47=models.CharField(max_length=50, null=True)
    BP47=models.CharField(max_length=50, null=True)
    RP47=models.CharField(max_length=50, null=True)
    LP47=models.CharField(max_length=50, null=True)
    CP46=models.CharField(max_length=50, null=True)
    TP46=models.CharField(max_length=50, null=True)
    BP46=models.CharField(max_length=50, null=True)
    RP46=models.CharField(max_length=50, null=True)
    LP46=models.CharField(max_length=50, null=True)
    CP45=models.CharField(max_length=50, null=True)
    TP45=models.CharField(max_length=50, null=True)
    BP45=models.CharField(max_length=50, null=True)
    RP45=models.CharField(max_length=50, null=True)
    LP45=models.CharField(max_length=50, null=True)
    CP44=models.CharField(max_length=50, null=True)
    TP44=models.CharField(max_length=50, null=True)
    BP44=models.CharField(max_length=50, null=True)
    RP44=models.CharField(max_length=50, null=True)
    LP44=models.CharField(max_length=50, null=True)
    CP43=models.CharField(max_length=50, null=True)
    TP43=models.CharField(max_length=50, null=True)
    BP43=models.CharField(max_length=50, null=True)
    RP43=models.CharField(max_length=50, null=True)
    LP43=models.CharField(max_length=50, null=True)
    CP42=models.CharField(max_length=50, null=True)
    TP42=models.CharField(max_length=50, null=True)
    BP42=models.CharField(max_length=50, null=True)
    RP42=models.CharField(max_length=50, null=True)
    LP42=models.CharField(max_length=50, null=True)
    CP41=models.CharField(max_length=50, null=True)
    TP41=models.CharField(max_length=50, null=True)
    BP41=models.CharField(max_length=50, null=True)
    RP41=models.CharField(max_length=50, null=True)
    LP41=models.CharField(max_length=50, null=True)
    CP21=models.CharField(max_length=50, null=True)
    TP21=models.CharField(max_length=50, null=True)
    BP21=models.CharField(max_length=50, null=True)
    RP21=models.CharField(max_length=50, null=True)
    LP21=models.CharField(max_length=50, null=True)
    CP22=models.CharField(max_length=50, null=True)
    TP22=models.CharField(max_length=50, null=True)
    BP22=models.CharField(max_length=50, null=True)
    RP22=models.CharField(max_length=50, null=True)
    LP22=models.CharField(max_length=50, null=True)
    CP23=models.CharField(max_length=50, null=True)
    TP23=models.CharField(max_length=50, null=True)
    BP23=models.CharField(max_length=50, null=True)
    RP23=models.CharField(max_length=50, null=True)
    LP23=models.CharField(max_length=50, null=True)
    CP24=models.CharField(max_length=50, null=True)
    TP24=models.CharField(max_length=50, null=True)
    BP24=models.CharField(max_length=50, null=True)
    RP24=models.CharField(max_length=50, null=True)
    LP24=models.CharField(max_length=50, null=True)
    CP25=models.CharField(max_length=50, null=True)
    TP25=models.CharField(max_length=50, null=True)
    BP25=models.CharField(max_length=50, null=True)
    RP25=models.CharField(max_length=50, null=True)
    LP25=models.CharField(max_length=50, null=True)
    CP26=models.CharField(max_length=50, null=True)
    TP26=models.CharField(max_length=50, null=True)
    BP26=models.CharField(max_length=50, null=True)
    RP26=models.CharField(max_length=50, null=True)
    LP26=models.CharField(max_length=50, null=True)
    CP27=models.CharField(max_length=50, null=True)
    TP27=models.CharField(max_length=50, null=True)
    BP27=models.CharField(max_length=50, null=True)
    RP27=models.CharField(max_length=50, null=True)
    LP27=models.CharField(max_length=50, null=True)
    CP28=models.CharField(max_length=50, null=True)
    TP28=models.CharField(max_length=50, null=True)
    BP28=models.CharField(max_length=50, null=True)
    RP28=models.CharField(max_length=50, null=True)
    LP28=models.CharField(max_length=50, null=True)
    CP61=models.CharField(max_length=50, null=True)
    TP61=models.CharField(max_length=50, null=True)
    BP61=models.CharField(max_length=50, null=True)
    RP61=models.CharField(max_length=50, null=True)
    LP61=models.CharField(max_length=50, null=True)
    CP62=models.CharField(max_length=50, null=True)
    TP62=models.CharField(max_length=50, null=True)
    BP62=models.CharField(max_length=50, null=True)
    RP62=models.CharField(max_length=50, null=True)
    LP62=models.CharField(max_length=50, null=True)
    CP63=models.CharField(max_length=50, null=True)
    TP63=models.CharField(max_length=50, null=True)
    BP63=models.CharField(max_length=50, null=True)
    RP63=models.CharField(max_length=50, null=True)
    LP63=models.CharField(max_length=50, null=True)
    CP64=models.CharField(max_length=50, null=True)
    TP64=models.CharField(max_length=50, null=True)
    BP64=models.CharField(max_length=50, null=True)
    RP64=models.CharField(max_length=50, null=True)
    LP64=models.CharField(max_length=50, null=True)
    CP65=models.CharField(max_length=50, null=True)
    TP65=models.CharField(max_length=50, null=True)
    BP65=models.CharField(max_length=50, null=True)
    RP65=models.CharField(max_length=50, null=True)
    LP65=models.CharField(max_length=50, null=True)
    CP71=models.CharField(max_length=50, null=True)
    TP71=models.CharField(max_length=50, null=True)
    BP71=models.CharField(max_length=50, null=True)
    RP71=models.CharField(max_length=50, null=True)
    LP71=models.CharField(max_length=50, null=True)
    CP72=models.CharField(max_length=50, null=True)
    TP72=models.CharField(max_length=50, null=True)
    BP72=models.CharField(max_length=50, null=True)
    RP72=models.CharField(max_length=50, null=True)
    LP72=models.CharField(max_length=50, null=True)
    CP73=models.CharField(max_length=50, null=True)
    TP73=models.CharField(max_length=50, null=True)
    BP73=models.CharField(max_length=50, null=True)
    RP73=models.CharField(max_length=50, null=True)
    LP73=models.CharField(max_length=50, null=True)
    CP74=models.CharField(max_length=50, null=True)
    TP74=models.CharField(max_length=50, null=True)
    BP74=models.CharField(max_length=50, null=True)
    RP74=models.CharField(max_length=50, null=True)
    LP74=models.CharField(max_length=50, null=True)
    CP75=models.CharField(max_length=50, null=True)
    TP75=models.CharField(max_length=50, null=True)
    BP75=models.CharField(max_length=50, null=True)
    RP75=models.CharField(max_length=50, null=True)
    LP75=models.CharField(max_length=50, null=True)
    CP31=models.CharField(max_length=50, null=True)
    TP31=models.CharField(max_length=50, null=True)
    BP31=models.CharField(max_length=50, null=True)
    RP31=models.CharField(max_length=50, null=True)
    LP31=models.CharField(max_length=50, null=True)
    CP32=models.CharField(max_length=50, null=True)
    TP32=models.CharField(max_length=50, null=True)
    BP32=models.CharField(max_length=50, null=True)
    RP32=models.CharField(max_length=50, null=True)
    LP32=models.CharField(max_length=50, null=True)
    CP33=models.CharField(max_length=50, null=True)
    TP33=models.CharField(max_length=50, null=True)
    BP33=models.CharField(max_length=50, null=True)
    RP33=models.CharField(max_length=50, null=True)
    LP33=models.CharField(max_length=50, null=True)
    CP34=models.CharField(max_length=50, null=True)
    TP34=models.CharField(max_length=50, null=True)
    BP34=models.CharField(max_length=50, null=True)
    RP34=models.CharField(max_length=50, null=True)
    LP34=models.CharField(max_length=50, null=True)
    CP35=models.CharField(max_length=50, null=True)
    TP35=models.CharField(max_length=50, null=True)
    BP35=models.CharField(max_length=50, null=True)
    RP35=models.CharField(max_length=50, null=True)
    LP35=models.CharField(max_length=50, null=True)
    CP36=models.CharField(max_length=50, null=True)
    TP36=models.CharField(max_length=50, null=True)
    BP36=models.CharField(max_length=50, null=True)
    RP36=models.CharField(max_length=50, null=True)
    LP36=models.CharField(max_length=50, null=True)
    CP37=models.CharField(max_length=50, null=True)
    TP37=models.CharField(max_length=50, null=True)
    BP37=models.CharField(max_length=50, null=True)
    RP37=models.CharField(max_length=50, null=True)
    LP37=models.CharField(max_length=50, null=True)
    CP38=models.CharField(max_length=50, null=True)
    TP38=models.CharField(max_length=50, null=True)
    BP38=models.CharField(max_length=50, null=True)
    RP38=models.CharField(max_length=50, null=True)
    LP38=models.CharField(max_length=50, null=True)
    estado=models.BooleanField(blank=True, null=True)


class cita(models.Model):
    idCita=models.AutoField(primary_key=True)
    idPaciente=models.ForeignKey(paciente, on_delete=models.CASCADE, null=True)
    idDoctor=models.ForeignKey(doctor, on_delete=models.CASCADE, null=True)
    fecha=models.DateField()
    hora=models.TimeField()
    estado=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=300)
    status = models.BooleanField(blank=True, null=True)

class consulta(models.Model):
    idConsulta=models.AutoField(primary_key=True)
    idCita=models.ForeignKey(cita, on_delete=models.CASCADE)
    motivo=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=300)
    temperatura=models.CharField(max_length=200, null=True)
    respiracion=models.CharField(max_length=200, null=True)
    presionArterial=models.CharField(max_length=200, null=True)
    pulso=models.CharField(max_length=200, null=True)
    frecuenciaCardiaca=models.CharField(max_length=200, null=True)
    frecuenciaRespiratoria=models.CharField(max_length=200, null=True)
    receta = models.CharField(max_length=250, null=True)

class tratamientoTemporal(models.Model):
    idTratamientoTemporal=models.AutoField(primary_key=True)
    idTratamiento=models.ForeignKey(tratamiento,on_delete=models.CASCADE)
    idPaciente=models.ForeignKey(paciente,on_delete=models.CASCADE)
    resumen=models.CharField(max_length=300, null=True)
    diagnostico=models.CharField(max_length=300, null=True)
    observacionDiagnostico=models.CharField(max_length=300, null=True)

class tratamientoRealizado(models.Model):
    idTratamientoRealizado=models.AutoField(primary_key=True)
    idTratamiento=models.ForeignKey(tratamiento,on_delete=models.CASCADE)
    idPaciente=models.ForeignKey(paciente,on_delete=models.CASCADE)
    idConsulta=models.ForeignKey(consulta, on_delete=models.CASCADE)
    conclusion=models.CharField(max_length=300, null=True)
    diagnostico=models.CharField(max_length=300, null=True)
    observacionDiagnostico=models.CharField(max_length=300, null=True)

class historial(models.Model):
    idHistorial=models.AutoField(primary_key=True)
    idDoctor=models.ForeignKey(doctor, on_delete=models.CASCADE)
    idOdontograma=models.ForeignKey(odontograma, on_delete=models.CASCADE, null=True)
    idPaciente=models.ForeignKey(paciente, on_delete=models.CASCADE)
    peso=models.CharField(max_length=200, null=True)
    talla=models.CharField(max_length=200, null=True)
    imc=models.CharField(max_length=200, null=True)
    temperatura=models.CharField(max_length=200, null=True)
    respiracion=models.CharField(max_length=200, null=True)
    presionArterial=models.CharField(max_length=200, null=True)
    pulso=models.CharField(max_length=200, null=True)
    frecuenciaCardiaca=models.CharField(max_length=200, null=True)
    frecuenciaRespiratoria=models.CharField(max_length=200, null=True)
    antecedentesPersonales=models.CharField(max_length=400, null=True)
    tiempoEnfermedad=models.CharField(max_length=150, null=True)
    motivoConsulta=models.CharField(max_length=300, null=True)
    signoPrincipal=models.CharField(max_length=300, null=True)
    antecedentePersonal=models.CharField(max_length=300, null=True)
    tratamientoOrtodoncia=models.CharField(max_length=10, null=True)
    descripcionTratamientoOrtodoncia=models.CharField(max_length=150, null=True)
    medicamento=models.CharField(max_length=10, null=True)
    descripcionMedicamento=models.CharField(max_length=150, null=True)
    alergiaMedicamento=models.CharField(max_length=10, null=True)
    descripcionAlergia=models.CharField(max_length=150, null=True)
    trastornoNervioso=models.CharField(max_length=10, null=True)
    descripcionTrastorno=models.CharField(max_length=150, null=True)
    status=models.BooleanField(null=True)


class alergia(models.Model):
    idAlergia=models.AutoField(primary_key=True)
    idHistorial = models.ForeignKey(historial, on_delete=models.CASCADE, null=True)
    nombre=models.CharField(max_length=200,null=True)
    observacion=models.CharField(max_length=200,null=True)



class usuario(models.Model):
    idUsuario=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=150)
    clave=models.CharField(max_length=150)
    tipo=models.CharField(max_length=150)

class ingresoUsuario(models.Model):
    idIngreso=models.AutoField(primary_key=True)
    idUsuario=models.ForeignKey(usuario, on_delete=models.CASCADE,null=True)
    fecha=models.DateField()

class estadoCuenta(models.Model):
    idEstado=models.AutoField(primary_key=True)
    idPaciente=models.ForeignKey(paciente,on_delete=models.CASCADE,null=True)
    fecha=models.DateField(null=True)
    abono=models.IntegerField(null=True)
    saldo=models.IntegerField(null=True)

# class historialPago(models.Model):
#     idHistorialPago=models.AutoField(primary_key=True)
#     idEstado=models.ForeignKey(estadoCuenta,on_delete=models.CASCADE)
#     abono=models.FloatField(null=True)
