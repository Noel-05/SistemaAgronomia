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
            'codigo_ciclo': forms.TextInput(attrs={'placeholder': 'Código Ciclo', 'autofocus': '', 'required': '', 'maxlength':'5', 'pattern': '[1-2]{1}[0-9]{4}', 'title': 'Ingreselo con el formato Numero de Ciclo (1 o 2) y Año calendario,   Ej: 12020. (Esto significa el Ciclo 1, del Año 2020)'}),
        }
        fields = {
            'codigo_ciclo': forms.IntegerField,
        }
        labels = {
            'codigo_ciclo': 'Codigo Ciclo',
        }

    def __init__(self, *args, **kwargs):
        super(CicloForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })
                


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class  EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        widgets = {
            'carnet_estudiante': forms.TextInput(attrs={'placeholder': 'Carnet Estudiante', 'autofocus': '', 'required': '', 'maxlength':'7', 'pattern': '([a-zA-Z]{2}[0-9]{5})', 'title': 'Ingrese el Carnet, Ej. AA99999.'}),
            'telefono_estudiante': forms.TextInput(attrs={'placeholder': 'Telefono Estudiante', 'autofocus': '', 'required': '', 'autocomplete': 'off', 'maxlength':'15', 'pattern': '[0-9]{8,15}', 'title': 'Ingrese el Telefono, Solo Numeros Enteros Sin Espacio.'}),
            'correo_estudiante': forms.TextInput(attrs={'placeholder': 'Correo Estudiante', 'autofocus': '', 'required': '', 'autocomplete': 'off', 'pattern': '^[a-z0-9!#$%&*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$'}),
            'nombre_estudiante': forms.TextInput(attrs={'placeholder': 'Nombres Estudiante', 'autofocus': '', 'autocomplete': 'off', 'required': '', 'maxlength':'50'}),
            'apellido_estudiante': forms.TextInput(attrs={'placeholder': 'Apellidos Estudiante', 'autofocus': '', 'autocomplete': 'off', 'required': '', 'maxlength':'50'}),
            'direccion_estudiante': forms.TextInput(attrs={'placeholder': 'Direccion Estudiante', 'autofocus': '', 'required': ''}),
            'sexo_estudiante': forms.Select(choices=sexo),
        }
        fields = {
            'carnet_estudiante': forms.CharField,
            'nombre_estudiante': forms.CharField,
            'apellido_estudiante': forms.CharField,
            'sexo_estudiante': forms.CharField,
            'telefono_estudiante': forms.IntegerField,
            'correo_estudiante': forms.CharField,
            'direccion_estudiante': forms.CharField,
        }
        labels = {
            'carnet_estudiante': 'Carnet',
            'nombre_estudiante':'Nombre',
            'apellido_estudiante':'Apellido',
            'sexo_estudiante': 'Sexo',
            'telefono_estudiante': 'Telefono',
            'correo_estudiante': 'Correo',
            'direccion_estudiante': 'Direccion',
        }

    def __init__(self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })

        self.fields['sexo_estudiante'].widget.attrs.update({
                'class': 'form-control'
                })


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class  EntidadExternForm(forms.ModelForm):
    class Meta:
        model = EntidadExterna
        widgets = {
            'codigo_entidad': forms.TextInput(attrs={'placeholder': 'Código Entidad', 'autofocus': '', 'required': '', 'maxlength':'10', 'title': 'Ingrese el Carnet, Ej. AA99999.'}),
            'nombre_entidad': forms.TextInput(attrs={'placeholder': 'Nombre Entidad', 'autofocus': '', 'autocomplete': 'off', 'required': '', 'maxlength':'100'}),
            'direccion_entidad': forms.TextInput(attrs={'placeholder': 'Dirección Entidad', 'autofocus': '', 'autocomplete': 'off', 'required': '', 'maxlength':'250'}),
            'telefono_entidad': forms.TextInput(attrs={'placeholder': 'Nombre Entidad', 'autofocus': '', 'required': '', 'autocomplete': 'off', 'maxlength':'15', 'pattern': '[0-9]{8,15}', 'title': 'Ingrese el Telefono, Solo Numeros Enteros Sin Espacio.'}),
        }
        fields = {
            'codigo_entidad': forms.CharField,
            'nombre_entidad': forms.CharField,
            'direccion_entidad': forms.CharField,
            'telefono_entidad': forms.IntegerField,
        }
        labels = {
            'codigo_entidad': 'Código',
            'nombre_entidad': 'Nombre',
            'direccion_entidad': 'Dirección',
            'telefono_entidad': 'Telefono',
        }

    def __init__(self, *args, **kwargs):
        super(EntidadExternForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class EstudioUniversitarioForm(forms.ModelForm):
    codigo_carrera = forms.ModelChoiceField(queryset=Carrera.objects.all().order_by('nombre_carrera'))
    codigo_ciclo = forms.ModelChoiceField(queryset=Ciclo.objects.all().order_by('codigo_ciclo'))
    carnet_estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all().order_by('carnet_estudiante'))

    class Meta:
        model = EstudioUniversitario
        widgets = {
            'porc_carrerar_aprob': forms.TextInput(attrs={'placeholder': 'Porcentaje Carrera Aprobado', 'autofocus': '', 'required': '', 'maxlength':'3', 'pattern': '([0-9]{1,3})', 'title': 'Ingrese el Pocentaje de Carrera Aprobado, Solo Numeros Enteros, No Coloque Signo de %.'}),
            'unidades_valorativas': forms.TextInput(attrs={'placeholder': 'Unidades Valorativas', 'autofocus': '', 'required': '',  'maxlength':'3', 'pattern': '([0-9]{1,3})', 'title': 'Ingrese la Cantidad de Unidades Valorativas Obtenidas.'}),
            'experiencia_areas_conoc': forms.TextInput(attrs={'placeholder': 'Experiencia en Areas Conocidas', 'autofocus': '', 'maxlength':'200', 'title': 'Si no tiene ninguna experiencia porfavor escriba "Ninguna".'}),
        }
        fields = {
            'carnet_estudiante': forms.CharField,
            'codigo_carrera': forms.CharField,
            'codigo_ciclo': forms.IntegerField,
            'porc_carrerar_aprob': forms.IntegerField,
            'unidades_valorativas': forms.IntegerField,
            'experiencia_areas_conoc': forms.CharField,
        }
        labels = {
            'carnet_estudiante': 'Carnet Estudiante',
            'codigo_carrera': 'Carrera Estudiante',
            'codigo_ciclo': 'Ciclo',
            'porc_carrerar_aprob': 'Porcentaje Carrera Aprobado',
            'unidades_valorativas': 'Unidades Valorativas',
            'experiencia_areas_conoc': 'Experiencia en Areas Conocidas',
        }

    def __init__(self, *args, **kwargs):
        super(EstudioUniversitarioForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })

        self.fields['carnet_estudiante'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Busca tu carnet en la siguiente lista, estos están ordenados en forma ascendente para una búsqueda más rápida. Por favor verifica que hayas seleccionado tu carnet correctamente.'
                })
        self.fields['codigo_carrera'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Selecciona la carrera a la que perteneces.'
                })
        self.fields['codigo_ciclo'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Selecciona el ciclo correspondiente a este año lectivo, este se divide en Número de ciclo (1 o 2) y Año calendario.'
                })

    def clean(self, *args, **kwargs):
        cleaned_data = super(EstudioUniversitarioForm, self).clean(*args, **kwargs)
        porc_carrerar_aprob = cleaned_data.get('porc_carrerar_aprob', None)
        if porc_carrerar_aprob is not None:
            if porc_carrerar_aprob < 60:
                self.add_error('porc_carrerar_aprob', 'Aun no esta apto para realizar el servicio social.')


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class SolicitudForm(forms.ModelForm):
    codigo_entidad = forms.ModelChoiceField(queryset=EntidadExterna.objects.all().order_by('nombre_entidad'))
    carnet_estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all().order_by('carnet_estudiante'))

    class Meta:
        model = Solicitud
        widgets = {
            'horas_semana': forms.TextInput(attrs={'placeholder': 'Horas a la Semana', 'autofocus': '', 'required': '', 'maxlength':'3', 'pattern': '([0-9]{1,3})', 'title': 'Ingrese el Total de Horas que realizara a la semana.'}),
            'dias_semana': forms.TextInput(attrs={'placeholder': 'Días a la Semana', 'autofocus': '', 'required': '',  'maxlength':'1', 'pattern': '([0-9]{1})', 'title': 'Ingrese el Total de Días que realizara a la semana.'}),
            'modalidad': forms.TextInput(attrs={'placeholder': 'Modalidad del Servicio', 'autofocus': '', 'required': '', 'maxlength':'30', 'pattern': '([a-zA-Záéíóú ]{3,30})', 'title': 'Ingrese la Modalidad en que desea realizar el Servicio Social.'}),
            'fecha_inicio': forms.TextInput(attrs={'placeholder': 'Fecha de Inicio', 'autocomplete': 'off', 'type':'date', 'min':'1940-01-01'}),
            'fecha_fin': forms.TextInput(attrs={'placeholder': 'Fecha de Finalización', 'autocomplete': 'off', 'type':'date', 'min':'1940-01-01', 'required':'false'}),
        }
        fields = {
            'carnet_estudiante': forms.CharField,
            'codigo_entidad': forms.CharField,
            'horas_semana': forms.CharField,
            'dias_semana': forms.CharField,
            'modalidad': forms.IntegerField,
            'fecha_inicio': forms.DateField,
            'fecha_fin': forms.DateField,
        }
        labels = {
            'carnet_estudiante': 'Carnet Estudiante',
            'codigo_entidad': 'Nombre de la Entidad',
            'horas_semana': 'Horas a la Semana',
            'dias_semana': 'Días a la Semana',
            'modalidad': 'Modalidad del Servicio',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_fin': 'Fecha Finalización',
        }

    def __init__(self, *args, **kwargs):
        super(SolicitudForm, self).__init__(*args, **kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })
        
        self.fields['carnet_estudiante'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Busca tu carnet en la siguiente lista, estos están ordenados en forma ascendente para una búsqueda más rápida. Por favor verifica que hayas seleccionado tu carnet correctamente.'
                })
        self.fields['codigo_entidad'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Selecciona la entidad en la que deseas realizar tu servicio social. Si no encuentras la que deseas puedes sugerir una presionando el botón.'
                })


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class EstadoSolicitudForm(forms.ModelForm):
    carnet_estudiante = forms.ModelChoiceField(queryset=Solicitud.objects.all().order_by('carnet_estudiante'))

    class Meta:
        model = EstadoSolicitud
        widgets = {
            'aceptado': forms.Select(choices=estado),
            'motivo': forms.TextInput(attrs={'placeholder': 'Motivo', 'autofocus': '', 'required': False}),
            'observaciones': forms.TextInput(attrs={'placeholder': 'Observaciones', 'autofocus': '', 'required': False}),
        }
        fields = {
            'carnet_estudiante': forms.CharField,
            'aceptado': forms.CharField,
            'motivo': forms.CharField,
            'observaciones': forms.CharField,
        }
        labels = {
            'carnet_estudiante': 'Carnet Estudiante',
            'aceptado': 'Estado de la Solicitud',
            'motivo': 'Motivo',
            'observaciones': 'Observaciones',
        }

    def __init__(self, *args, **kwargs):
        super(EstadoSolicitudForm, self).__init__(*args, **kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })
        
        self.fields['carnet_estudiante'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Busca el carnet del estudiante en la siguiente lista, estos están ordenados en forma ascendente para una búsqueda más rápida. Por favor verificar que se haya seleccionado el carnet correcto.'
                })

        self.fields['aceptado'].widget.attrs.update({
                'class': 'form-control',
                })


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class ArchivosEstudianteForm(forms.ModelForm):
    class Meta:
        model = ArchivosEstudiante
        widgets = {
            'documento': forms.ClearableFileInput
        }
        fields = {
            'carnet_estudiante': forms.HiddenInput,
            'documento': forms.FileField,
        }
        labels = {
            'documento': 'Documento'
        }
    def __init__(self, *args, **kwargs):
        super(ArchivosEstudianteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
            })
        self.fields['carnet_estudiante'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Busca tu carnet en la siguiente lista, estos están ordenados en forma ascendente para una búsqueda más rápida. Por favor verifica que hayas seleccionado tu carnet correctamente.'
        })
        self.fields['carnet_estudiante'].disabled = True

        self.fields['documento'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'tittle': 'Seleccione el documento a almacenar en la ventana de selección'
        })


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class CarreraForm(forms.ModelForm):
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all().order_by('codigoDepartamento'))

    class Meta:
        model = Carrera
        widgets = {
            'codigo_carrera': forms.TextInput(attrs={'placeholder': 'Código Carrera', 'autofocus': '', 'required': '', 'maxlength':'6'}),
            'nombre_carrera': forms.TextInput(attrs={'placeholder': 'Carrera', 'autofocus': '', 'required': ''}),
            'departamento': forms.TextInput(attrs={'placeholder': 'Departamento', 'autofocus': '', 'required': ''}),
        }
        fields = {
            'codigo_carrera': forms.IntegerField,
            'nombre_carrera': forms.CharField,
            'departamento': forms.CharField,
        }
        labels = {
            'codigo_carrera': 'Codigo Carrera',
            'nombre_carrera': 'Carrera',
            'departamento': 'Departamento',
        }

    def __init__(self, *args, **kwargs):
        super(CarreraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })

            self.fields['codigo_carrera'].widget.attrs.update({
                'pattern': '([A-Z]{3}[0-9]{3})', 
                'title': 'Ingrese el Codigo, Ej. IID115.'
                })

            self.fields['nombre_carrera'].widget.attrs.update({
                'pattern': '[A-Za-záéíóú ]{1,100}', 
                'title': 'Ingrese el Codigo, Ej. Ingeniería Industrial.'
                })

            self.fields['departamento'].widget.attrs.update({
                'pattern': '[A-Za-záéíóú ]{1,100}', 
                'title': 'Ingrese el Codigo, Ej. Escuela Sistemas.'
                })

        self.fields['departamento'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Selecciona el departamento al que pertenece esta carrrera.'
                })


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class ServicioSocialForm(forms.ModelForm):
    carnet_estudiante = forms.ModelChoiceField(queryset=Solicitud.objects.all().order_by('carnet_estudiante'))
    carnet_docente = forms.ModelChoiceField(queryset=Docente.objects.all().order_by('carnet_docente'))
    dui_asesor_externo = forms.ModelChoiceField(queryset=AsesorExterno.objects.all().order_by('dui_asesor_externo'))
    codigo_proyecto = forms.ModelChoiceField(queryset=Proyecto.objects.all().order_by('codigo_proyecto'))
    class Meta:
        model = ServicioSocial
        widgets = {
            #'carnet_estudiante': forms.TextInput(attrs={'placeholder': 'Carnet estudiante', 'autofocus': '', 'required': '', 'maxlength':'7'}),
            #'carnet_docente': forms.TextInput(attrs={'placeholder': 'Carnet docente', 'autofocus': '', 'required': '', 'maxlength':'7'}),
            #'dui_asesor_externo': forms.TextInput(attrs={'placeholder': 'Dui sesor externo', 'autofocus': '', 'required': ''}),
            #'codigo_proyecto': forms.TextInput(attrs={'placeholder': 'Codigo proyecto', 'autofocus': '', 'required': ''}),

        }
        fields = {
            'carnet_estudiante': forms.CharField,
            'carnet_docente': forms.CharField,
            'dui_asesor_externo': forms.CharField,
            'codigo_proyecto': forms.CharField,
        }
        labels = {
            'carnet_estudiante':'Carnet Estudiante',
            'carnet_docente':'Carnet Docente',
            'dui_asesor_externo':'Dui asesor externo',
            'codigo_proyecto':'Código proyecto',
        }

    def __init__(self, *args, **kwargs):
        super(ServicioSocialForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })

            self.fields['carnet_estudiante'].widget.attrs.update({     
                'class': 'form-control', 
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Busca tu carnet en la siguiente lista, estos están ordenados en forma ascendente para una búsqueda más rápida. Por favor verifica que hayas seleccionado tu carnet correctamente.'
                })
            self.fields['carnet_docente'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Selecciona el docente para tutor del servicio social.'
                })
            self.fields['dui_asesor_externo'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Selecciona el Asesor Externo para el Servicio Social, si NO esta registrado porfavor registralo en el boton de al lado.'
                })
            self.fields['codigo_proyecto'].widget.attrs.update({
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'data-html': 'true',
                'data-placement': 'right',
                'title': 'Selecciona el proyecto a realizar para el servicio social.'
                })
            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Asesor Externo

class AsesorExternoForm(forms.ModelForm):
    class Meta:
        model = AsesorExterno
        widgets = {
            """'dui_asesor_externo' forms.TextInput(attrs={'placeholder': 'dui ', 'autofocus': '', 'required': '', 'maxlength':'5', 'pattern': '[1-2]{1}[0-9]{4}', 'title': 'Ingreselo con el formato Numero de Ciclo (1 o 2) y Año calendario,   Ej: 12020. (Esto significa el Ciclo 1, del Año 2020)'}),"""
        }
        fields = {
            'dui_asesor_externo': forms.CharField,
            'nombre_asesor_externo': forms.CharField,
            'apellido_asesor_externo': forms.CharField,
            'cargo_asesor_externo': forms.CharField,
        }
        labels = {
            'dui_asesor_externo': 'DUI Asesor Externo' ,
            'nombre_asesor_externo': 'Nombre Asesor Externo' ,
            'apellido_asesor_externo': 'Apellido Asesor Externo',
            'cargo_asesor_externo': 'Cargo Asesor Externo',
        }
        
    def __init__(self, *args, **kwargs):
        super(AsesorExternoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })

 #Asesor Interno       

class AsesorInternoForm(forms.ModelForm):
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all().order_by('codigoDepartamento'))
    class Meta:
        model = Docente
        widgets = {
            """'dui_asesor_externo' forms.TextInput(attrs={'placeholder': 'dui ', 'autofocus': '', 'required': '', 'maxlength':'5', 'pattern': '[1-2]{1}[0-9]{4}', 'title': 'Ingreselo con el formato Numero de Ciclo (1 o 2) y Año calendario,   Ej: 12020. (Esto significa el Ciclo 1, del Año 2020)'}),"""
        }
        fields = {
            'carnet_docente': forms.CharField,
            'nombre_docente': forms.CharField,
            'apellido_docente': forms.CharField,
            'departamento': forms.CharField,
            'nombre_rol': forms.CharField,
            
        }
        labels = {
            'carnet_docente': 'Carnet del docente' ,
            'nombre_docente': 'Nombre del docente' ,
            'apellido_docente': 'Apellido de docente',
            'departamento': 'Departamento',
            'nombre_rol': 'Nombre Rol',
            
        }
        
    def __init__(self, *args, **kwargs):
        super(AsesorInternoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Agregar Horas Sociales

class HorasSocialesForm(forms.ModelForm):
    class Meta:
        model = HorasSociales
        widgets = {
            'fecha_servicio': forms.TextInput(attrs={'placeholder': 'Fecha de Servicio', 'autocomplete': 'off', 'type':'date', 'min':'1940-01-01'}),
            'actividad_realizada': forms.TextInput(attrs={'placeholder': 'Actividad Realizada', 'autofocus': '', 'autocomplete': 'off', 'required': '', 'maxlength':'50'}),

        }
        fields = {
            'carnet_estudiante': forms.HiddenInput,        
            'fecha_servicio': forms.DateField,
            'hora_entrada': forms.CharField,
            'actividad_realizada': forms.CharField,
            'hora_salida': forms.CharField,
        }
        labels = {
            'fecha_servicio': 'Fecha de Servicio' ,
            'hora_entrada': 'Hora de Entrada' ,
            'actividad_realizada': 'Actividad Realizada',
            'hora_salida': 'Hora de Salida',
        }
        
    def __init__(self, *args, **kwargs):
        super(HorasSocialesForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })
        self.fields['carnet_estudiante'].widget.attrs.update({
                'class': 'form-control',
        })
        self.fields['carnet_estudiante'].disabled = True


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        widgets = {
            'codigo_proyecto': forms.TextInput(attrs={'placeholder': 'Código Proyecto', 'autofocus': '', 'required': '', 'maxlength':'10'}),
            'descripcion_proyecto': forms.TextInput(attrs={'placeholder': 'Descripción Proyecto', 'autofocus': '', 'required': ''}),
            
        }
        fields = {
           'codigo_proyecto': forms.IntegerField,
           'descripcion_proyecto': forms.CharField,
        }   
        labels = {
            'codigo_proyecto': 'Codigo Proyecto',
            'descripcion_proyecto': 'Descripción Proyecto',
        }

    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })

            self.fields['codigo_proyecto'].widget.attrs.update({
                'pattern': '([A-Z0-9]{6,10})', 
                'title': 'Ingrese el Codigo, deben ser 10 digitos maximo Ej. PAS1001.'
                })

            self.fields['descripcion_proyecto'].widget.attrs.update({
                'pattern': '[A-Za-záéíóú0-9 ]{1,100}', 
                'title': 'Ingrese el Codigo, Ej. Ayudante de Catedra para la materia Sistemas Contables.'
                })
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class  ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        widgets = {
            """'carnet_estudiante': forms.TextInput(attrs={'placeholder': 'Carnet Estudiante', 'autofocus': '', 'required': '', 'maxlength':'7', 'pattern': '([a-zA-Z]{2}[0-9]{5})', 'title': 'Ingrese el Carnet, Ej. AA99999.'}),
            'telefono_estudiante': forms.TextInput(attrs={'placeholder': 'Telefono Estudiante', 'autofocus': '', 'required': '', 'autocomplete': 'off', 'maxlength':'15', 'pattern': '[0-9]{8,15}', 'title': 'Ingrese el Telefono, Solo Numeros Enteros Sin Espacio.'}),
            'correo_estudiante': forms.TextInput(attrs={'placeholder': 'Correo Estudiante', 'autofocus': '', 'required': '', 'autocomplete': 'off', 'pattern': '^[a-z0-9!#$%&*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$'}),
            'nombre_estudiante': forms.TextInput(attrs={'placeholder': 'Nombres Estudiante', 'autofocus': '', 'autocomplete': 'off', 'required': '', 'maxlength':'50'}),
            'apellido_estudiante': forms.TextInput(attrs={'placeholder': 'Apellidos Estudiante', 'autofocus': '', 'autocomplete': 'off', 'required': '', 'maxlength':'50'}),
            'direccion_estudiante': forms.TextInput(attrs={'placeholder': 'Direccion Estudiante', 'autofocus': '', 'required': ''}),
            'sexo_estudiante': forms.Select(choices=sexo),"""
        }
        fields = {
            'correlativo': forms.IntegerField,
            'carnet_estudiante': forms.CharField,
            'nombre_actividad': forms.CharField,
        }
        labels = {
            'correlativo': 'Correlativo',
            'carnet_estudiante': 'Carnet del estudiante',
            'nombre_actividad': 'Actividad'

        }

    """def init(self, *args, **kwargs):
         super(ActividadForm, self).init(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
                })

       self.fields['carnet_estudiante'].widget.attrs.update({
                'class': 'form-control'
                })"""
    def init(self, *args, **kwargs):
        super(ActividadForm, self).init(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'material-control tooltips-general'
            })