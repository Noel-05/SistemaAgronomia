from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.postgres.fields import ArrayField

sexo = [('M', 'M'), ('F', 'F'), ]
estado = [('Abierto', 'Abierto'), ('Cerrado', 'Cerrado')]

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        widgets = {
            'apellido_paciente': forms.TextInput(attrs={'placeholder': 'Primer apellido'}),
            'segApellPaciente': forms.TextInput(attrs={'placeholder': 'Segundo apellido'}),
            'nombre_paciente': forms.TextInput(attrs={'placeholder': 'Primer nombre'}),
            'segNombrePaciente': forms.TextInput(attrs={'placeholder': 'Segundo nombre'}),
            'fecha_nacimiento_paciente': forms.TextInput(
                attrs={'placeholder': 'Fecha de nacimiento', 'autocomplete': 'off','type':'date', 'min':'1940-01-01'}),
            'edad_paciente': forms.NumberInput(attrs={'placeholder': 'Edad paciente'}),
            'sexo_paciente': forms.Select(choices=sexo),
            'direccion_paciente': forms.TextInput(attrs={'placeholder': 'Dirección'}),
            'telefono_paciente': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            'lugar_trabajo_paciente': forms.TextInput(attrs={'placeholder': 'Lugar de trabajo'}),
            'ocupacion_paciente': forms.TextInput(attrs={'placeholder': 'Ocupación'}),
            'responsable_paciente': forms.TextInput(attrs={'placeholder': 'Responsable'}),
            'fecha_expediente': forms.TextInput(
                attrs={'placeholder': 'Fecha de expediente', 'autocomplete': 'off','type':'date', 'min':'1940-01-01'}),
            'histoMedica': forms.Textarea,
            'histoOdonto': forms.Textarea,
            'codigo_expediente': forms.NumberInput(
                attrs={'placeholder': 'Código expediente', 'autofocus': 'on', 'autocomplete': 'off',
                       'required': 'true'}),
            'estado_expediente': forms.Select(choices=estado),
        }
        fields = {
            'apellido_paciente': forms.CharField,
            'segApellPaciente': forms.CharField,
            'nombre_paciente': forms.CharField,
            'segNombrePaciente': forms.CharField,
            'fecha_nacimiento_paciente': forms.DateField,
            'edad_paciente': forms.IntegerField,
            'sexo_paciente': forms.CharField,
            'direccion_paciente': forms.CharField,
            'telefono_paciente': forms.CharField,
            'ocupacion_paciente': forms.CharField,
            'lugar_trabajo_paciente': forms.CharField,
            'responsable_paciente': forms.CharField,
            'codigo_expediente': forms.IntegerField,
            'estado_expediente': forms.CharField,
            'fecha_expediente': forms.DateField,
            'histoMedica': forms.TextInput,
            'histoOdonto': forms.TextInput,
        }
        labels = {
            'codigo_paciente': 'Código paciente: ',
            'apellido_paciente': 'Primer apellido: ',
            'segApellPaciente': 'Segundo apellido: ',
            'nombre_paciente': 'Primer nombre: ',
            'segNombrePaciente': 'Segundo nombre: ',
            'edad_paciente': 'Edad paciente: ',
            'fecha_nacimiento_paciente': 'Fecha de nacimiento: ',
            'sexo_paciente': 'Sexo: ',
            'direccion_paciente': 'Dirección: ',
            'telefono_paciente': 'Teléfono: ',
            'ocupacion_paciente': 'Ocupación Paciente: ',
            'lugar_trabajo_paciente': 'Lugar de trabajo: ',
            'responsable_paciente': 'Responsable: ',
            'codigo_expediente': 'Código expediente: ',
            'estado_expediente': 'Estado expediente: ',
            'fecha_expediente': 'Fecha expediente: ',
            'histoMedica': 'Historia medica',
            'histoOdonto': 'Historia odontologíca',
        }
