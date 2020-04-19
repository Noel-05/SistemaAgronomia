from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

class Ciclo(models.Model):
    codigo_ciclo = models.IntegerField(primary_key=True, null=False)
    ciclo_lectivo = models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.codigo_ciclo.__str__()

class Alumno(models.Model):
    codigo_alumno = models.IntegerField(primary_key=True, null=False)
    carnet_alumno = models.CharField(max_length=7, null=False) 
    nombre_alumno = models.CharField(max_length=200, null=False)
    sexo_alumno = models.CharField(max_length=1, null=False)
    telefono_alumno = models.IntegerField(null=False)
    correo_alumno = models.CharField(max_length=50, null=False)
    direccion_alumno = models.CharField(max_length=50, null=False)
    carrera_alumno = models.CharField(max_length=50, null=False)
    porc_carr_apro = models.IntegerField(null=False)
    unidades_valorativas = models.IntegerField(null=False)
    experiencias_alumno = models.CharField(max_length=50, null=False)
    horas_semana = models.IntegerField(null=False)
    dias_semana = models.IntegerField(null=False)
    propuesta_entidad = models.CharField(max_length=50, null=False)
    propuesta_modalidad = models.CharField(max_length=50, null=False)
    fecha_inicio = models.DateField(null=False)
    estado_expediente = models.CharField(max_length=10, null=False)
    motivo = models.CharField(max_length=50, null=True)
    observaciones = models.CharField(max_length=50, null=True)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.carnet_alumno