from django.db import transaction
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.core import serializers
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *
from .forms import *
from .formularios import *
import time
from django.conf import settings
from apps.usuario.views import *


# Vista para el menu de inicio
def index(request, username):

    prb_btn = EstadoSolicitud.objects.filter(carnet_estudiante = username)

    buscar = []
    i=0
    while(i < len(prb_btn)):
        buscar.append((prb_btn[i].aceptado))
        i+=1
    
    resp = "No"
    for b in buscar:
        if (b == "Aceptado"):
            resp = "Si"
        else:
            resp = "No"

    context = {
        'resp' : resp,
    }

    return render(
        request,
        'base/base.html',
        context,
    )


#-----------------------------------------------------------------------------------------------


def consultaCiclo(request):
    ciclo_list=Ciclo.objects.order_by('codigo_ciclo')


    # Para asignar si es Ciclo Par o Impar
    query = Ciclo.objects.order_by('codigo_ciclo')
    codigos=[]
    i=0
    while(i < len(query)):
        codigos.append((query[i].codigo_ciclo))
        i+=1
    for c in codigos:
        tot = c - 10000
        if tot < 10000:
            tipo = "Impar"
        else:
            tipo = "Par"
        cod = c
        guarda = Ciclo(codigo_ciclo=c, tipo_ciclo=tipo)
        guarda.save()
        
        
    context = {
        'ciclo_list': ciclo_list,
    }
    return render(
        request,
        'app1/Ciclo.html', context
    )

class crearCiclo(LoginAMixin, CreateView):
    template_name = 'app1/crear_ciclo.html'
    form_class = CicloForm
    success_url = reverse_lazy('proyeccionsocial:consulta_ciclo')

class editarCiclo(LoginAMixin, UpdateView):
    model = Ciclo
    template_name = 'app1/crear_ciclo.html'
    form_class = CicloForm
    success_url = reverse_lazy('proyeccionsocial:consulta_ciclo')

class eliminarCiclo(LoginAMixin, DeleteView):
    model = Ciclo
    template_name = 'app1/eliminar_ciclo.html'
    success_url = reverse_lazy('proyeccionsocial:consulta_ciclo')


#-----------------------------------------------------------------------------------------------


def consultaEstudiante(request, username):
    queryset = Estudiante.objects.filter(carnet_estudiante = username)

    prb_btn = EstadoSolicitud.objects.filter(carnet_estudiante = username)

    buscar = []
    i=0
    while(i < len(prb_btn)):
        buscar.append((prb_btn[i].aceptado))
        i+=1
    
    resp = "No"
    for b in buscar:
        if (b == "Aceptado"):
            resp = "Si"
        else:
            resp = "No"

    suma = " "
    if len(queryset) == 0:
        suma = " "

    estudiante_list=Estudiante.objects.order_by('carnet_estudiante')
    context = {
        'estudiante_list': estudiante_list,
        'queryset': queryset,
        'suma': suma,
        'resp': resp,
    }
    return render(
        request,
        'app1/Estudiante.html', context
    )


def crearEstudiante(request, username):
    if request.method == 'POST':

        carnet = request.POST['carnet']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        sexo = request.POST['sexo']

        estudiante = Estudiante(carnet_estudiante=carnet, nombre_estudiante=nombres, apellido_estudiante=apellidos, direccion_estudiante=direccion, correo_estudiante=correo, telefono_estudiante=telefono, sexo_estudiante=sexo)
        estudiante.save()

        return HttpResponseRedirect(reverse_lazy('proyeccionsocial:consulta_estudiante', kwargs={'username': username}))
    
    else:

        return render(
            request,
            'app1/Crear_Estudiante.html'
        )

#class crearEstudiante(CreateView):
#    template_name = 'app1/Crear_Estudiante.html'
#    form_class = EstudianteForm
#    def get_success_url(self):
#      username = self.kwargs['username']
#      return reverse_lazy('proyeccionsocial:consulta_estudiante', kwargs={'username': username})

    #success_url = "/proyeccionsocial/consultaEstudioUniversitario/{username}/"
    #success_url = reverse_lazy('proyeccionsocial:consulta_estudio_universitario')


class editarEstudiante(LoginPEAMixin, UpdateView):
    model = Estudiante
    template_name = 'app1/Crear_Estudiante.html'
    form_class = EstudianteForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estudiante', kwargs={'username': username})


class eliminarEstudiante(LoginAMixin, DeleteView):
    model = Estudiante
    template_name = 'app1/eliminar_estudiante.html'
    
    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estudiante', kwargs={'username': username})


#-----------------------------------------------------------------------------------------------


class crearEntidadExterna(CreateView):
    template_name = 'app1/Crear_Entidad_Externa.html'
    form_class = EntidadExternForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:crear_solicitud_servicio_social', kwargs={'username': username})


#-----------------------------------------------------------------------------------------------


# Busqueda de Estudiante
def consultaEstudianteBuscar(request):
    carnet_estudiante = request.POST['carnet_estudiante']
    if request.method == 'POST':
        estudiante_busc = Estudiante.objects.filter(carnet_estudiante = carnet_estudiante)
        
        suma = " " 
        if len(estudiante_busc) == 0:
            suma = " "

        contexto = {'estudiante_busc': estudiante_busc,
        'suma': suma,
        }

        return render(request, 'app1/Estudiante.html', contexto)


#-----------------------------------------------------------------------------------------------


def consultaEstudioUniversitario(request, username):
    queryset = EstudioUniversitario.objects.filter(carnet_estudiante = username)

    prb_btn = EstadoSolicitud.objects.filter(carnet_estudiante = username)

    buscar = []
    i=0
    while(i < len(prb_btn)):
        buscar.append((prb_btn[i].aceptado))
        i+=1
    
    resp = "No"
    for b in buscar:
        if (b == "Aceptado"):
            resp = "Si"
        else:
            resp = "No"

    suma = " "
    if len(queryset) == 0:
        suma = " "

    estudios_list = EstudioUniversitario.objects.order_by('codigo_carrera')
    context = {
        'estudios_list': estudios_list,
        'queryset': queryset,
        'suma': suma,
        'resp': resp,
    }
    return render(
        request,
        'app1/EstudioUniversitario.html', context
    )


def crearEstudioUniversitario(request, username):
    if request.method == 'POST':

        carnet = request.POST['carnet']
        carrera = request.POST['carrera']
        ciclo = request.POST['ciclo']
        porcentaje = request.POST['porcentaje']
        unidades = request.POST['unidades']
        experiencia = request.POST['experiencia']

        estudio = EstudioUniversitario(carnet_estudiante=Estudiante.objects.get(carnet_estudiante=carnet), codigo_carrera=Carrera.objects.get(codigo_carrera=carrera), codigo_ciclo=Ciclo.objects.get(codigo_ciclo=ciclo), porc_carrerar_aprob=porcentaje, unidades_valorativas=unidades, experiencia_areas_conoc=experiencia)
        estudio.save()

        return HttpResponseRedirect(reverse_lazy('proyeccionsocial:consulta_estudio_universitario', kwargs={'username': username}))
    
    else:

        estudiantes = Estudiante.objects.order_by('carnet_estudiante')
        carreras = Carrera.objects.order_by('codigo_carrera')
        ciclos = Ciclo.objects.order_by('codigo_ciclo')

        context = {
            'ciclos': ciclos,
            'carreras': carreras,
            'estudiantes': estudiantes,
        }

        return render(
            request,
            'app1/Crear_Estudio_Universitario.html',
            context
        )


#class crearEstudioUniversitario(LoginEAMixin, CreateView):
#    template_name = 'app1/Crear_Estudio_Universitario.html'
#    form_class = EstudioUniversitarioForm

#    def get_success_url(self):
#      username = self.kwargs['username']
#      return reverse_lazy('proyeccionsocial:consulta_estudio_universitario', kwargs={'username': username})
    #success_url = "/proyeccionsocial/consultaEstudioUniversitario/{username}/"
    #success_url = reverse_lazy('proyeccionsocial:consulta_estudio_universitario')


class editarEstudioUniversitario(LoginEAMixin, UpdateView):
    model = EstudioUniversitario
    template_name = 'app1/Crear_Estudio_Universitario.html'
    form_class = EstudioUniversitarioForm
    
    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estudio_universitario', kwargs={'username': username})
    #success_url = "/proyeccionsocial/consultaEstudioUniversitario/{username}/"
    #success_url = reverse_lazy('proyeccionsocial:consulta_estudio_universitario')


class eliminarEstudioUniversitario(LoginAMixin, DeleteView):
    model = EstudioUniversitario
    template_name = 'app1/eliminar_estudio_universitario.html'

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estudio_universitario', kwargs={'username': username})
    #success_url = reverse_lazy('proyeccionsocial:consulta_estudio_universitario')


#-----------------------------------------------------------------------------------------------


# Busqueda de Estudiante
def consultaEstudioUniversitarioBuscar(request):
    carnet_estudiante = request.POST['carnet_estudiante']
    if request.method == 'POST':
        estudiante_busc = EstudioUniversitario.objects.filter(carnet_estudiante = carnet_estudiante)
        
        suma = " "
        if len(estudiante_busc) == 0:
            suma = " "

        contexto = {'estudiante_busc': estudiante_busc,
        'suma': suma,
        }

        return render(request, 'app1/EstudioUniversitario.html', contexto)


#-----------------------------------------------------------------------------------------------


def consultaSolicitudServicioSocial(request, username):
    queryset = Solicitud.objects.filter(carnet_estudiante = username)

    prb_btn = EstadoSolicitud.objects.filter(carnet_estudiante = username)

    buscar = []
    i=0
    while(i < len(prb_btn)):
        buscar.append((prb_btn[i].aceptado))
        i+=1
    
    resp = "No"
    for b in buscar:
        if (b == "Aceptado"):
            resp = "Si"
        else:
            resp = "No"

    suma = " "
    if len(queryset) == 0:
        suma = " "

    solicitudes_list = Solicitud.objects.order_by('carnet_estudiante')
    context = {
        'solicitudes_list': solicitudes_list,
        'queryset': queryset,
        'suma': suma,
        'resp': resp,
    }
    return render(
        request,
        'app1/Solicitud.html', context
    )


def crearSolicitudServicioSocial(request, username):
    if request.method == 'POST':

        carnet = request.POST['carnet']
        entidad = request.POST['entidad']
        horas = request.POST['horas']
        dias = request.POST['dias']
        modalidad = request.POST['modalidad']
        inicio = request.POST['inicio']
        fin = request.POST['fin']

        solicitud = Solicitud(carnet_estudiante=Estudiante.objects.get(carnet_estudiante=carnet), codigo_entidad=EntidadExterna.objects.get(codigo_entidad=entidad), horas_semana=horas, dias_semana=dias, modalidad=modalidad, fecha_inicio=inicio, fecha_fin=fin)
        solicitud.save()

        return HttpResponseRedirect(reverse_lazy('proyeccionsocial:consulta_solicitud_servicio_social', kwargs={'username': username}))
    
    else:

        estudiantes = Estudiante.objects.order_by('carnet_estudiante')
        entidades = EntidadExterna.objects.order_by('codigo_entidad')

        context = {
            'estudiantes': estudiantes,
            'entidades': entidades,
        }

        return render(
            request,
            'app1/Crear_Solicitud_Servicio_Social.html',
            context
        )

#class crearSolicitudServicioSocial(LoginEAMixin, CreateView):
#    template_name = 'app1/Crear_Solicitud_Servicio_Social.html'
#    form_class = SolicitudForm

#    def get_success_url(self):
#      username = self.kwargs['username']
#      return reverse_lazy('proyeccionsocial:consulta_solicitud_servicio_social', kwargs={'username': username})


class editarSolicitudServicioSocial(LoginEAMixin, UpdateView):
    model = Solicitud
    template_name = 'app1/Crear_Solicitud_Servicio_Social.html'
    form_class = SolicitudForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_solicitud_servicio_social', kwargs={'username': username})

    # Para el boton Solicitudes del Base para Administrador
class editarSolicitudServicioSocial2(LoginPAMixin, UpdateView):
    model = Solicitud
    template_name = 'app1/Crear_Solicitud_Servicio_Social_Consulta.html'
    form_class = SolicitudForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estado_solicitud_servicio_social', kwargs={'username': username})


class eliminarSolicitudServicioSocial(LoginPAMixin, DeleteView):
    model = Solicitud
    template_name = 'app1/eliminar_solicitud_servicio_social.html'
    
    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_solicitud_servicio_social', kwargs={'username': username})

# Para el boton Solicitudes del Base para Administrador
class eliminarSolicitudServicioSocial2(LoginPAMixin, DeleteView):
    model = Solicitud
    template_name = 'app1/eliminar_solicitud_servicio_social_consulta.html'
    
    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estado_solicitud_servicio_social', kwargs={'username': username})


#-----------------------------------------------------------------------------------------------


# Busqueda de Estudiante
def consultaSolicitudServicioSocialBuscar(request):
    carnet_estudiante = request.POST['carnet_estudiante']
    if request.method == 'POST':
        estudiante_busc = Solicitud.objects.filter(carnet_estudiante = carnet_estudiante)
        
        suma = " "
        if len(estudiante_busc) == 0:
            suma = " "

        contexto = {'estudiante_busc': estudiante_busc,
        'suma': suma,
        }

        return render(request, 'app1/Solicitud.html', contexto)


#-----------------------------------------------------------------------------------------------


def consultaEstadoSolicitudServicioSocial(request, username):
    queryset = Solicitud.objects.filter(carnet_estudiante = username)

    suma = " "
    if len(queryset) == 0:
        suma = " "

    solicitudes_list = Solicitud.objects.order_by('carnet_estudiante')
    context = {
        'solicitudes_list': solicitudes_list,
        'queryset': queryset,
        'suma': suma,
    }
    return render(
        request,
        'app1/SolicitudConsulta.html', context
    )

def consultaEstadoSolicitudServicioSocialConsulta(request, username):
    querysetEstado = EstadoSolicitud.objects.filter(carnet_estudiante = username)

    estadoSolicitudes_list = EstadoSolicitud.objects.order_by('carnet_estudiante')
    context = {
        'estadoSolicitudes_list': estadoSolicitudes_list,
        'querysetEstado': querysetEstado,
    }
    return render(
        request,
        'app1/SolicitudEstadoConsulta.html', context
    )

# Para el boton Solicitudes del Base para Administrador
def consultaEstadoSolicitudServicioSocialBuscar(request):
    carnet_estudiante = request.POST['carnet_estudiante']
    if request.method == 'POST':
        estudiante_busc = Solicitud.objects.filter(carnet_estudiante = carnet_estudiante)
        
        suma = " "
        if len(estudiante_busc) == 0:
            suma = " "

        contexto = {'estudiante_busc': estudiante_busc,
        'suma': suma,
        }

        return render(request, 'app1/SolicitudConsulta.html', contexto)

def consultaEstadoSolicitudServicioSocialBuscar2(request):
    carnet_estudiante = request.POST['carnet_estudiante']
    if request.method == 'POST':
        estudiante_busc = EstadoSolicitud.objects.filter(carnet_estudiante = carnet_estudiante)
        
        suma = " "
        if len(estudiante_busc) == 0:
            suma = " "

        contexto = {
            'estudiante_busc': estudiante_busc,
            'suma': suma,
        }

        return render(request, 'app1/SolicitudEstadoConsulta.html', contexto)


# Para el boton Solicitudes del Base para Administrador
class crearEstadoSolicitudServicioSocial(LoginPAMixin, CreateView):
    template_name = 'app1/Crear_Estado_Solicitud_Servicio_Social.html'
    form_class = EstadoSolicitudForm

    def get_initial(self):
        return {"carnet_estudiante": self.kwargs.get("pk")}

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_solicitud_servicio_social', kwargs={'username': username})


class crearEstadoSolicitudServicioSocial2(LoginPAMixin, CreateView):
    template_name = 'app1/Crear_Estado_Solicitud_Servicio_Social_Consulta.html'
    form_class = EstadoSolicitudForm

    def get_initial(self):
        return {"carnet_estudiante": self.kwargs.get("pk")}

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_estado_solicitud_servicio_social_consulta', kwargs={'username': username})


class editarEstadoSolicitudServicioSocial(LoginPAMixin, UpdateView):
    model = EstadoSolicitud
    template_name = 'app1/Crear_Estado_Solicitud_Servicio_Social_Consulta.html'
    form_class = EstadoSolicitudForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estado_solicitud_servicio_social_consulta', kwargs={'username': username})


class eliminarEstadoSolicitudServicioSocial(LoginPAMixin, DeleteView):
    model = EstadoSolicitud
    template_name = 'app1/eliminar_estado_solicitud_servicio_social.html'
    
    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estado_solicitud_servicio_social_consulta', kwargs={'username': username})


#-----------------------------------------------------------------------------------------------

class documentosEstudianteListView(ListView):
    model = ArchivosEstudiante
    template_name = 'app1/documentos_estudiante.html'
    context_object_name = 'archivos'

    def get_queryset(self):
        return ArchivosEstudiante.objects.filter(carnet_estudiante=self.kwargs.get("pk"))

class agregarDocumentos(CreateView):
    model = ArchivosEstudiante
    form_class = ArchivosEstudianteForm
    template_name = 'app1/agregar_documentos.html'

    def get_initial(self):
        return {"carnet_estudiante": self.kwargs.get("pk")}

    def get_success_url(self):
      username = str(self.object.carnet_estudiante)
      return reverse_lazy('proyeccionsocial:listar_documentos', kwargs={'pk': username})

class eliminarDocumento(DeleteView):
    model = ArchivosEstudiante
    template_name = 'app1/eliminar_documento.html'

    def get_success_url(self):
        username = str(self.object.carnet_estudiante)
        return reverse_lazy('proyeccionsocial:listar_documentos', kwargs={'pk': username})


#-----------------------------------------------------------------------------------------------


def consultaCarrera(request):
        carrera_list=Carrera.objects.order_by('codigo_carrera')
        context = {
        'carrera_list': carrera_list,
    }
        return render(
        request,
        'app1/Carrera.html', context
    )

class crearCarrera(LoginAMixin, CreateView):
    template_name = 'app1/crear_carrera.html'
    form_class = CarreraForm
    success_url = reverse_lazy('proyeccionsocial:consulta_carrera')

class editarCarrera(LoginAMixin, UpdateView):
    model = Carrera
    template_name = 'app1/crear_carrera.html'
    form_class = CarreraForm
    success_url = reverse_lazy('proyeccionsocial:consulta_carrera')

class eliminarCarrera(LoginAMixin, DeleteView):
    model = Carrera
    template_name = 'app1/eliminar_carrera.html'
    success_url = reverse_lazy('proyeccionsocial:consulta_carrera')


#-----------------------------------------------------------------------------------------------


def consultaServicioSocial(request, username):
    queryset = ServicioSocial.objects.filter(carnet_estudiante = username)

    prb_btn = EstadoSolicitud.objects.filter(carnet_estudiante = username)

    buscar = []
    i=0
    while(i < len(prb_btn)):
        buscar.append((prb_btn[i].aceptado))
        i+=1
    
    resp = "No"
    for b in buscar:
        if (b == "Aceptado"):
            resp = "Si"
        else:
            resp = "No"

    suma = "No"
    if len(queryset) == 0:
        suma = " "

    servicio_social_list=ServicioSocial.objects.order_by('carnet_estudiante')
    context = {
        'servicio_social_list': servicio_social_list,
        'queryset': queryset,
        'suma': suma,
        'resp': resp,
    }
    return render(
        request,
        'app1/ServicioSocial.html', context
    )

class crearServicioSocial(LoginPEAMixin, CreateView):
    template_name = 'app1/crear_servicio_social.html'
    form_class = ServicioSocialForm

    def get_initial(self):
        username = self.kwargs['username']
        return {"carnet_estudiante": username}

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_servicio_social', kwargs={'username': username})


class crearServicioSocialAdmin(LoginPEAMixin, CreateView):
    template_name = 'app1/crear_servicio_social.html'
    form_class = ServicioSocialAdminForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_servicio_social', kwargs={'username': username})


class editarServicioSocial(LoginEAMixin, UpdateView):
    model = ServicioSocial
    template_name = 'app1/crear_servicio_social.html'
    form_class = ServicioSocialForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_servicio_social', kwargs={'username': username})


class eliminarServicioSocial(LoginAMixin, DeleteView):
    model = ServicioSocial
    template_name = 'app1/eliminar_servicio_social.html'

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_servicio_social', kwargs={'username': username})


# Busqueda de ServicioSocial
def consultaServicioSocialBuscar(request):
    carnet_estudiante = request.POST['carnet_estudiante']
    if request.method == 'POST':
        estudiante_busc = ServicioSocial.objects.filter(carnet_estudiante = carnet_estudiante)
        
        suma = " "
        if len(estudiante_busc) == 0:
            suma = " "

        contexto = {'estudiante_busc': estudiante_busc,
        'suma': suma,
        }

        return render(request, 'app1/ServicioSocial.html', contexto)


    
#Asesor Externo ---------------------------------------------------------------------------


def consultaAsesorExterno(request):
    asesoresExternos=AsesorExterno.objects.order_by('dui_asesor_externo')
    
    if asesoresExternos:
        existenRegistros=True
        diccionario={"asesores_externos": asesoresExternos, "existenRegistros":existenRegistros}
    else:
        existenRegistros=False
        diccionario={"existenRegistros": existenRegistros}
    
    return render(request, 'app1/AsesorExterno.html', diccionario)

class crearAsesorExterno(LoginPEAMixin, CreateView):
    template_name = 'app1/crear_asesor_externo.html'
    form_class = AsesorExternoForm
    success_url = reverse_lazy('proyeccionsocial:consulta_asesor_externo')

    
class crearAsesorExternoEstudiante(LoginPEAMixin, CreateView):
    template_name = 'app1/crear_asesor_externo_estudiante.html'
    form_class = AsesorExternoForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:crear_servicio_social', kwargs={'username': username})
    

class editarAsesorExterno(LoginAMixin, UpdateView):
    model = AsesorExterno
    template_name = 'app1/crear_asesor_externo.html'
    form_class = AsesorExternoForm

    def get_success_url(self):
      return reverse_lazy('proyeccionsocial:consulta_asesor_externo')

class eliminarAsesorExterno(LoginAMixin, DeleteView):
    model = AsesorExterno
    template_name = 'app1/eliminar_asesor_externo.html'
    
    def get_success_url(self):
      return reverse_lazy('proyeccionsocial:consulta_asesor_externo')
    

#Docente (Asesor Interno) ---------------------------------------------------------------------------


def consultaAsesorInterno(request):
    docentes=Docente.objects.order_by('carnet_docente')
    
    if docentes:
        existenRegistros=True
        diccionario={"asesores_internos": docentes, "existenRegistros":existenRegistros}
    
    else:
        existenRegistros=False
        diccionario={"existenRegistros": existenRegistros}
    
    return render(request, 'app1/AsesorInterno.html', diccionario)

class crearAsesorInterno(LoginAMixin, CreateView):
    template_name = 'app1/crear_asesor_interno.html'
    form_class = AsesorInternoForm
    success_url = reverse_lazy('proyeccionsocial:consulta_asesor_interno')
    
class editarAsesorInterno(LoginAMixin, UpdateView):
    model = Docente
    template_name = 'app1/crear_asesor_interno.html'
    form_class = AsesorInternoForm

    def get_success_url(self):
      
      return reverse_lazy('proyeccionsocial:consulta_asesor_interno')

class eliminarAsesorInterno(LoginAMixin, DeleteView):
    model = Docente
    template_name = 'app1/eliminar_asesor_interno.html'
    
    def get_success_url(self):
      return reverse_lazy('proyeccionsocial:consulta_asesor_interno')


#-----------------------------------------------------------------------------------------------
#Horas Sociales


class horasSocialesListView(LoginPEAMixin, ListView):
    model = HorasSociales
    template_name = 'app1/horas_sociales.html'
    context_object_name = 'horas_sociales'


    def get_queryset(self):
        return HorasSociales.objects.filter(carnet_estudiante=self.kwargs.get("pk"))


class agregarHorasSociales(LoginPAMixin, CreateView):
    model = HorasSociales
    form_class = HorasSocialesForm
    template_name = 'app1/agregar_horas_sociales.html'

    def get_initial(self):
        return {"carnet_estudiante": self.kwargs.get("pk")}

    def get_success_url(self):
        username = str(self.object.carnet_estudiante)
        return reverse_lazy('proyeccionsocial:listar_horas_sociales', kwargs={'pk': username})


class editarHorasSociales(UpdateView):
    model = HorasSociales
    form_class = HorasSocialesForm
    template_name = 'app1/agregar_horas_sociales.html'

    def get_success_url(self):
        username = str(self.object.carnet_estudiante)
        return reverse_lazy('proyeccionsocial:listar_horas_sociales', kwargs={'pk': username})


class eliminarHorasSociales(DeleteView):
    model = HorasSociales
    template_name = 'app1/eliminar_horas_sociales.html'

    def get_success_url(self):
        username = str(self.object.carnet_estudiante)
        return reverse_lazy('proyeccionsocial:listar_horas_sociales', kwargs={'pk': username})


#-----------------------------------------------------------------------------------------------


def consultaProyecto(request):
        proyecto_list=Proyecto.objects.order_by('codigo_proyecto')
        context = {
        'proyecto_list': proyecto_list,
    }
        return render(
        request,
        'app1/Proyecto.html', context
    )


class crearProyecto(LoginAMixin, CreateView):
    template_name = 'app1/crear_proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('proyeccionsocial:consulta_proyecto')


class editarProyecto(LoginAMixin, UpdateView):
    model = Proyecto
    template_name = 'app1/crear_proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('proyeccionsocial:consulta_proyecto')


class eliminarProyecto(LoginAMixin, DeleteView):
    model = Proyecto
    template_name = 'app1/eliminar_proyecto.html'
    success_url = reverse_lazy('proyeccionsocial:consulta_proyecto')


#-----------------------------------------------------------------------------------------------


def consultaProyectoBuscar(request):
    codigo_proyecto = request.POST['codigo_proyecto']
    if request.method == 'POST':
        proyecto_busc = Proyecto.objects.filter(codigo_proyecto = codigo_proyecto)
        
        suma = " " 
        if len(proyecto_busc) == 0:
            suma = " "

        contexto = {'proyecto_busc': proyecto_busc,
        'suma': suma,
        }

        return render(request, 'app1/Proyecto.html', contexto)


#-----------------------------------------------------------------------------------------------


def consultaActividad(request, username):
    
    actividades=Actividad.objects.filter(carnet_estudiante=username)
    actividadesAdmin=Actividad.objects.order_by('carnet_estudiante')
    
    if actividades:
        existenRegistros=True
        diccionario={
            "actividades": actividades, 
            "existenRegistros": existenRegistros, 
            "actividadesAdmin": actividadesAdmin,
        }
    else:
        existenRegistros=False
        diccionario={
            "existenRegistros": existenRegistros,
            "actividadesAdmin": actividadesAdmin,
        }

    diccionario2={
        "actividadesAdmin": actividadesAdmin,
    }
    
    return render(request, 'app1/Actividad.html', diccionario, diccionario2)


class crearActividad(LoginEAMixin, CreateView):
    template_name = 'app1/crear_actividad.html'
    form_class = ActividadForm

    def get_initial(self):
        username = self.kwargs['username']
        return {"carnet_estudiante": username}

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_actividad', kwargs={'username': username})
    # def get_success_url(self):
    #   username= str(self.object.carnet_estudiante)
    #   return reverse_lazy('proyeccionsocial:consulta_actividad', kwargs={'username': username})
    

class crearActividadAdmin(LoginEAMixin, CreateView):
    template_name = 'app1/crear_actividad.html'
    form_class = ActividadAdminForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_actividad', kwargs={'username': username})


class editarActividad(LoginEAMixin, UpdateView):
    model = Actividad
    template_name = 'app1/crear_actividad.html'
    form_class = ActividadForm
    def get_success_url(self):
        username= str(self.object.carnet_estudiante)
        return reverse_lazy('proyeccionsocial:consulta_actividad', kwargs={'username': username})


class eliminarActividad(LoginAMixin, DeleteView):
    model = Actividad
    template_name = 'app1/eliminar_actividad.html'
    def get_success_url(self):
        username= str(self.object.carnet_estudiante)
        return reverse_lazy('proyeccionsocial:consulta_actividad', kwargs={'username': username})
