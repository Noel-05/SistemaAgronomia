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

class crearCiclo(CreateView):
    template_name = 'app1/crear_ciclo.html'
    form_class = CicloForm
    success_url = reverse_lazy('proyeccionsocial:consulta_ciclo')

class editarCiclo(UpdateView):
    model = Ciclo
    template_name = 'app1/crear_ciclo.html'
    form_class = CicloForm
    success_url = reverse_lazy('proyeccionsocial:consulta_ciclo')

class eliminarCiclo(DeleteView):
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

class crearEstudiante(CreateView):
    template_name = 'app1/Crear_Estudiante.html'
    form_class = EstudianteForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_estudiante', kwargs={'username': username})


class editarEstudiante(UpdateView):
    model = Estudiante
    template_name = 'app1/Crear_Estudiante.html'
    form_class = EstudianteForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estudiante', kwargs={'username': username})


class eliminarEstudiante(DeleteView):
    model = Estudiante
    template_name = 'app1/eliminar_estudiante.html'
    
    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estudiante', kwargs={'username': username})


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



class crearEstudioUniversitario(CreateView):
    template_name = 'app1/Crear_Estudio_Universitario.html'
    form_class = EstudioUniversitarioForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_estudio_universitario', kwargs={'username': username})
    #success_url = "/proyeccionsocial/consultaEstudioUniversitario/{username}/"
    #success_url = reverse_lazy('proyeccionsocial:consulta_estudio_universitario')


class editarEstudioUniversitario(UpdateView):
    model = EstudioUniversitario
    template_name = 'app1/Crear_Estudio_Universitario.html'
    form_class = EstudioUniversitarioForm
    
    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estudio_universitario', kwargs={'username': username})
    #success_url = "/proyeccionsocial/consultaEstudioUniversitario/{username}/"
    #success_url = reverse_lazy('proyeccionsocial:consulta_estudio_universitario')


class eliminarEstudioUniversitario(DeleteView):
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

class crearSolicitudServicioSocial(CreateView):
    template_name = 'app1/Crear_Solicitud_Servicio_Social.html'
    form_class = SolicitudForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_solicitud_servicio_social', kwargs={'username': username})


class editarSolicitudServicioSocial(UpdateView):
    model = Solicitud
    template_name = 'app1/Crear_Solicitud_Servicio_Social.html'
    form_class = SolicitudForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_solicitud_servicio_social', kwargs={'username': username})

    # Para el boton Solicitudes del Base para Administrador
class editarSolicitudServicioSocial2(UpdateView):
    model = Solicitud
    template_name = 'app1/Crear_Solicitud_Servicio_Social_Consulta.html'
    form_class = SolicitudForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estado_solicitud_servicio_social', kwargs={'username': username})


class eliminarSolicitudServicioSocial(DeleteView):
    model = Solicitud
    template_name = 'app1/eliminar_solicitud_servicio_social.html'
    
    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_solicitud_servicio_social', kwargs={'username': username})

# Para el boton Solicitudes del Base para Administrador
class eliminarSolicitudServicioSocial2(DeleteView):
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
class crearEstadoSolicitudServicioSocial(CreateView):
    template_name = 'app1/Crear_Estado_Solicitud_Servicio_Social.html'
    form_class = EstadoSolicitudForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_solicitud_servicio_social', kwargs={'username': username})

class crearEstadoSolicitudServicioSocial2(CreateView):
    template_name = 'app1/Crear_Estado_Solicitud_Servicio_Social_Consulta.html'
    form_class = EstadoSolicitudForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_estado_solicitud_servicio_social_consulta', kwargs={'username': username})


class editarEstadoSolicitudServicioSocial(UpdateView):
    model = EstadoSolicitud
    template_name = 'app1/Crear_Estado_Solicitud_Servicio_Social_Consulta.html'
    form_class = EstadoSolicitudForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_estado_solicitud_servicio_social_consulta', kwargs={'username': username})


class eliminarEstadoSolicitudServicioSocial(DeleteView):
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

class crearCarrera(CreateView):
    template_name = 'app1/crear_carrera.html'
    form_class = CarreraForm
    success_url = reverse_lazy('proyeccionsocial:consulta_carrera')

class editarCarrera(UpdateView):
    model = Carrera
    template_name = 'app1/crear_carrera.html'
    form_class = CarreraForm
    success_url = reverse_lazy('proyeccionsocial:consulta_carrera')

class eliminarCarrera(DeleteView):
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

class crearServicioSocial(CreateView):
    template_name = 'app1/crear_servicio_social.html'
    form_class = ServicioSocialForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_servicio_social', kwargs={'username': username})


class editarServicioSocial(UpdateView):
    model = ServicioSocial
    template_name = 'app1/crear_servicio_social.html'
    form_class = ServicioSocialForm

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_servicio_social', kwargs={'username': username})


class eliminarServicioSocial(DeleteView):
    model = ServicioSocial
    template_name = 'app1/eliminar_servicio_social.html'

    def get_success_url(self):
      username = self.kwargs['pk']
      return reverse_lazy('proyeccionsocial:consulta_servicio_social', kwargs={'username': username})

# Busqueda de Estudiante
def consultaServicioSocialBuscar(request):
    carnet_estudiante = request.POST['carnet_estudiante']
    if request.method == 'POST':
       estudiante_busc = ServicioSocial.objects.filter(carnet_estudiante = carnet_estudiante)
        
    suma = " "
    if len( estudiante_busc) == 0:
        suma = " "
    
    contexto = {'estudiante_busc ': estudiante_busc,
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

class crearAsesorExterno(CreateView):
    template_name = 'app1/crear_asesor_externo.html'
    form_class = AsesorExternoForm
    success_url = reverse_lazy('proyeccionsocial:consulta_asesor_externo')

    
class crearAsesorExternoEstudiante(CreateView):
    template_name = 'app1/crear_asesor_externo_estudiante.html'
    form_class = AsesorExternoForm

    def get_success_url(self):
      username = self.kwargs['username']
      return reverse_lazy('proyeccionsocial:consulta_servicio_social', kwargs={'username': username})
    

class editarAsesorExterno(UpdateView):
    model = AsesorExterno
    template_name = 'app1/crear_asesor_externo.html'
    form_class = AsesorExternoForm

    def get_success_url(self):
      return reverse_lazy('proyeccionsocial:consulta_asesor_externo')

class eliminarAsesorExterno(DeleteView):
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

class crearAsesorInterno(CreateView):
    template_name = 'app1/crear_asesor_interno.html'
    form_class = AsesorInternoForm
    success_url = reverse_lazy('proyeccionsocial:consulta_asesor_interno')
    
class editarAsesorInterno(UpdateView):
    model = Docente
    template_name = 'app1/crear_asesor_interno.html'
    form_class = AsesorInternoForm

    def get_success_url(self):
      
      return reverse_lazy('proyeccionsocial:consulta_asesor_interno')

class eliminarAsesorInterno(DeleteView):
    model = Docente
    template_name = 'app1/eliminar_asesor_interno.html'
    
    def get_success_url(self):
      return reverse_lazy('proyeccionsocial:consulta_asesor_interno')


#-----------------------------------------------------------------------------------------------
