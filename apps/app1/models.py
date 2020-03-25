from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

class Expediente(models.Model):
    codigo_expediente = models.IntegerField(primary_key=True, null=False)
    apellido_paciente = models.CharField(max_length=50, null=False)
    segApellPaciente = models.CharField(max_length=50, null=False)
    nombre_paciente = models.CharField(max_length=50, null=False)
    segNombrePaciente = models.CharField(max_length=50, null=False)
    edad_paciente = models.IntegerField(null=False)
    sexo_paciente = models.CharField(max_length=1, null=False)
    direccion_paciente = models.CharField(max_length=200, null=False)
    telefono_paciente = models.CharField(max_length=8, null=False)
    ocupacion_paciente = models.CharField(max_length=50, null=False)
    lugar_trabajo_paciente = models.CharField(max_length=100, null=True)
    responsable_paciente = models.CharField(max_length=50, null=False)
    fecha_nacimiento_paciente = models.DateField(null=False)
    fecha_expediente = models.DateField(null=False)
    estado_expediente = models.CharField(max_length=50, null=False)
    histoMedica = models.CharField(max_length=300, null=False)
    histoOdonto = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.nombre_paciente