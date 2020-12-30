import os

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Ciclo(models.Model):
    codigo_ciclo = models.IntegerField(primary_key=True, null=False)
    tipo_ciclo = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.codigo_ciclo.__str__()



class Departamento(models.Model):
    codigoDepartamento = models.CharField(primary_key=True, max_length=10, null=False)
    nombreDepartamento = models.CharField(max_length=100, null=False)
    nombreJefeDepartamento = models.CharField(max_length=50, null=False)
    apellidoJefeDepartamento = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombreDepartamento



class Carrera(models.Model):
    codigo_carrera = models.CharField(primary_key=True, max_length=10, null=False)
    nombre_carrera = models.CharField(max_length=100, null=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_carrera



class Estudiante(models.Model):
    carnet_estudiante = models.CharField(primary_key=True, max_length=7, null=False)
    nombre_estudiante = models.CharField(max_length=50, null=False)
    apellido_estudiante = models.CharField(max_length=50, null=False)
    sexo_estudiante = models.CharField(max_length=1, null=False)
    telefono_estudiante = models.IntegerField(null=False)
    correo_estudiante = models.CharField(max_length=100, null=False)
    direccion_estudiante = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.carnet_estudiante



class EstudioUniversitario(models.Model):
    carnet_estudiante = models.OneToOneField(Estudiante, primary_key=True, unique=True, on_delete = models.CASCADE)
    codigo_carrera = models.ForeignKey(Carrera, on_delete = models.CASCADE)
    codigo_ciclo = models.ForeignKey(Ciclo, on_delete = models.CASCADE)
    porc_carrerar_aprob = models.IntegerField(null=False)
    unidades_valorativas = models.IntegerField(null=False)
    experiencia_areas_conoc = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.carnet_estudiante.__str__()




class EntidadExterna(models.Model):
    codigo_entidad = models.CharField(primary_key=True, max_length=10, null=False)
    nombre_entidad = models.CharField(max_length=100, null=False)
    direccion_entidad = models.CharField(max_length=250, null=False)
    telefono_entidad = models.IntegerField(null=False)

    def __str__(self):
        return self.nombre_entidad 



class Solicitud(models.Model):
    carnet_estudiante = models.OneToOneField(Estudiante, unique=True, primary_key=True, on_delete = models.CASCADE)
    codigo_entidad = models.ForeignKey(EntidadExterna, on_delete = models.CASCADE)
    horas_semana = models.IntegerField(null=False)
    dias_semana = models.IntegerField(null=False)
    modalidad = models.CharField(max_length=30, null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=True)

    def __str__(self):
        return self.carnet_estudiante.__str__()   



class EstadoSolicitud(models.Model):
    carnet_estudiante = models.OneToOneField(Solicitud, unique=True, primary_key=True, on_delete = models.CASCADE)
    aceptado = models.CharField(max_length=30, null=False)
    motivo = models.CharField(max_length=200, null=True, blank=True)
    observaciones = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.carnet_estudiante.__str__() 



class AsesorExterno(models.Model):
    dui_asesor_externo = models.CharField(primary_key=True, max_length=10, null=False)
    nombre_asesor_externo = models.CharField(max_length=50, null=False)
    apellido_asesor_externo = models.CharField(max_length=50, null=False)
    cargo_asesor_externo = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nombre_asesor_externo.__str__() +' '+ self.apellido_asesor_externo.__str__()



class Rol(models.Model):
    nombre_rol = models.CharField(primary_key=True, max_length=25, null=False)
    descripcion_rol = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.nombre_rol


class Docente(models.Model):
    carnet_docente = models.CharField(primary_key=True, max_length=10, null=False)
    nombre_docente = models.CharField(max_length=50, null=False)
    apellido_docente = models.CharField(max_length=50, null=False)
    nombre_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_docente.__str__() +' '+ self.apellido_docente.__str__()
        


class Proyecto(models.Model):
    codigo_proyecto = models.CharField(primary_key=True, max_length=10, null=False)
    descripcion_proyecto = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.codigo_proyecto.__str__() +' - '+ self.descripcion_proyecto.__str__()



class ServicioSocial(models.Model):
    carnet_estudiante = models.OneToOneField(Solicitud, primary_key=True, unique=True, on_delete=models.CASCADE)
    carnet_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    dui_asesor_externo = models.ForeignKey(AsesorExterno, on_delete=models.CASCADE)
    codigo_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.carnet_estudiante.__str__()


def crear_subcarpeta(instance, filename):
    return '/'.join([str(instance.carnet_estudiante), filename])


class ArchivosEstudiante(models.Model):
    carnet_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    documento = models.FileField(upload_to=crear_subcarpeta, null=True, blank=True)

    def filename(self):
        return os.path.basename(self.documento.name)

    def __str__(self):
        return self.carnet_estudiante


@receiver(post_delete, sender=ArchivosEstudiante)
def submission_delete(sender, instance, **kwargs):
    instance.documento.delete(False)