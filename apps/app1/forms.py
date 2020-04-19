from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.postgres.fields import ArrayField

sexo = [('M', 'M'), ('F', 'F'), ]
estado = [('Aceptado', 'Aceptado'), ('Denegado', 'Denegado')]


class CicloForm(forms.ModelForm):
    class Meta:
        model = Ciclo
        widgets = {
            'codigo_ciclo': forms.TextInput(attrs={'placeholder': 'Código Ciclo', 'autofocus': '', 'required': ''}),
            'ciclo_lectivo': forms.TextInput(attrs={'placeholder': 'Ciclo Lectivo', 'autofocus': '', 'required': ''}),
        }
        fields = {
            'codigo_ciclo': forms.IntegerField,
            'ciclo_lectivo': forms.CharField,
        }
        labels = {
            'codigo_ciclo': 'Codigo Ciclo',
            'ciclo_lectivo': 'Ciclo Lectivo',
        }

    def __init__(self, *args, **kwargs):
        super(CicloForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })

class AlumnoForm(forms.ModelForm):
    ciclo = forms.ModelChoiceField(queryset=Ciclo.objects.all())
    class Meta:
        model = Alumno
        widgets = {
            'codigo_alumno': forms.TextInput(attrs={'placeholder': 'Código Alumno', 'autofocus': '', 'required': ''}),
            'carnet_alumno': forms.TextInput(attrs={'placeholder': 'Carnet Alumno', 'autofocus': '', 'required': ''}),
            'nombre_alumno': forms.TextInput(attrs={'placeholder': 'Nombre Alumno', 'autofocus': '', 'required': ''}),
            'sexo_alumno': forms.Select(choices=sexo),
            'telefono_alumno': forms.TextInput(attrs={'placeholder': 'Telefono Alumno', 'autofocus': '', 'required': ''}),
            'correo_alumno': forms.TextInput(attrs={'placeholder': 'Correo Alumno', 'autofocus': '', 'required': ''}),
            'direccion_alumno': forms.TextInput(attrs={'placeholder': 'Direccion Alumno', 'autofocus': '', 'required': ''}),
            'carrera_alumno': forms.TextInput(attrs={'placeholder': 'Carrera Alumno', 'autofocus': '', 'required': ''}),
            'porc_carr_apro': forms.TextInput(attrs={'placeholder': 'Porcentaje Carrera', 'autofocus': '', 'required': ''}), 
            'unidades_valorativas': forms.TextInput(attrs={'placeholder': 'Unidades Valorativas', 'autofocus': '', 'required': ''}),
            'experiencias_alumno': forms.TextInput(attrs={'placeholder': 'Experiencia Alumno', 'autofocus': '', 'required': ''}),
            'horas_semana': forms.TextInput(attrs={'placeholder': 'Horas Por Semana', 'autofocus': '', 'required': ''}),
            'dias_semana': forms.TextInput(attrs={'placeholder': 'Dias Por Semana', 'autofocus': '', 'required': ''}),
            'propuesta_entidad': forms.TextInput(attrs={'placeholder': 'Propuesta Entidad', 'autofocus': '', 'required': ''}),
            'propuesta_modalidad': forms.TextInput(attrs={'placeholder': 'Propuesta Modalidad', 'autofocus': '', 'required': ''}),
            'fecha_inicio': forms.TextInput(attrs={'placeholder': 'Fecha de Cita', 'autocomplete': 'off', 'type':'date', 'min':'1940-01-01'}),
            'estado_expediente': forms.Select(choices=estado),
            'motivo': forms.Textarea,
            'observaciones': forms.Textarea,
        }
        fields = {
            'codigo_alumno': forms.CharField,
            'carnet_alumno': forms.CharField,
            'nombre_alumno': forms.CharField,
            'sexo_alumno': forms.CharField,
            'telefono_alumno': forms.IntegerField,
            'correo_alumno': forms.CharField,
            'direccion_alumno': forms.CharField,
            'carrera_alumno': forms.CharField,
            'porc_carr_apro': forms.IntegerField,
            'ciclo': forms.IntegerField,
            'unidades_valorativas': forms.IntegerField,
            'experiencias_alumno': forms.CharField,
            'horas_semana': forms.IntegerField,
            'dias_semana': forms.IntegerField,
            'propuesta_entidad': forms.CharField,
            'propuesta_modalidad': forms.CharField,
            'fecha_inicio': forms.DateField,
            'estado_expediente': forms.CharField,
            'motivo': forms.CharField,
            'observaciones': forms.CharField,
        }
        labels = {
            'codigo_alumno': 'Codigo',
            'carnet_alumno': 'Carnet',
            'nombre_alumno':'Nombre',
            'sexo_alumno': 'Sexo',
            'telefono_alumno': 'Telefono',
            'correo_alumno': 'Correo',
            'direccion_alumno': 'Direccion',
            'carrera_alumno': 'Carrera',
            'porc_carr_apro': 'Porcentaje Carrera',
            'unidades_valorativas': 'Unidades Valorativas',
            'ciclo': 'Ciclo',
            'experiencias_alumno': 'Experiencia',
            'horas_semana': 'Horas por Semana',
            'dias_semana': 'Dias por Semana',
            'propuesta_entidad': 'Propuesta Entidad',
            'propuesta_modalidad': 'Propuesta Modalidad',
            'fecha_inicio': 'Fecha Inicio',
            'estado_expediente': 'Estado',
            'motivo': 'Motivo',
            'observaciones': 'Observaciones',
        }