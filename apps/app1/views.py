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
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from .models import *
from .forms import *
from io import BytesIO
import time


# Vista para el menu de inicio
def index(request):
    return render(
        request,
        'base/base.html',
    )

#-----------------------------------------------------------------------------------------------

def consultaCiclo(request):
    ciclo_list=Ciclo.objects.order_by('codigo_ciclo')
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

def consultaEstudiante(request):
    estudiante_list=Estudiante.objects.order_by('carnet_estudiante')
    context = {
        'estudiante_list': estudiante_list,
    }
    return render(
        request,
        'app1/Estudiante.html', context
    )

class crearEstudiante(CreateView):
    template_name = 'app1/crear_estudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('proyeccionsocial:consulta_estudiante')

class editarEstudiante(UpdateView):
    model = Estudiante
    template_name = 'app1/crear_estudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('proyeccionsocial:consulta_estudiante')

class eliminarEstudiante(DeleteView):
    model = Estudiante
    template_name = 'app1/eliminar_estudiante.html'
    success_url = reverse_lazy('proyeccionsocial:consulta_estudiante')

#-----------------------------------------------------------------------------------------------


def consultaEstudioUniversitario(request):
    estudios_list=EstudioUniversitario.objects.order_by('codigo_carrera')
    context = {
        'estudios_list': estudios_list,
    }
    return render(
        request,
        'app1/EstudioUniversitario.html', context
    )

class crearEstudioUniversitario(CreateView):
    template_name = 'app1/crear_estudio_universitario.html'
    form_class = EstudioUniversitarioForm
    success_url = reverse_lazy('proyeccionsocial:consulta_estudio_universitario')

class editarEstudioUniversitario(UpdateView):
    model = EstudioUniversitario
    template_name = 'app1/crear_estudio_universitario.html'
    form_class = EstudioUniversitarioForm
    success_url = reverse_lazy('proyeccionsocial:consulta_estudio_universitario')

class eliminarEstudioUniversitario(DeleteView):
    model = EstudioUniversitario
    template_name = 'app1/eliminar_estudio_universitario.html'
    success_url = reverse_lazy('proyeccionsocial:consulta_estudio_universitario')

#-----------------------------------------------------------------------------------------------

class generarF1(ListView):
    model = Estudiante
    template_name = 'app1/Estudiante.html'
    context_object_name = 'estudiante'
    success_url = reverse_lazy('proyeccionsocial:generar_F1')  
     
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen1 = 'static/img/logoUPSAgro.png'
        archivo_imagen2 = 'static/img/logoUES.jpg'

        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen1, 50, 730, 125, 90,preserveAspectRatio=True) 
        pdf.drawImage(archivo_imagen2, 430, 720, 125, 90,preserveAspectRatio=True) 

        # Establecemos el tamaño de letra en 8 y el tipo de letra Helvetica en negrita
        # Luego en drawString se colocan las coordenadas X Y de donde se quiere poner
        # el texto, el eje Y inicia en la parte inferior izquierda, ahi es el punto (0, 0)
        pdf.setFont("Helvetica-Bold", 8)
        pdf.drawString(248, 780, u"UNIVERSIDAD DE EL SALVADOR")

        pdf.setFont("Helvetica-Bold", 8)
        pdf.drawString(232, 770, u"FACULTAD DE CIENCIAS AGRONOMICAS")  

        pdf.setFont("Helvetica-Bold", 8)
        pdf.drawString(234, 760, u"UNIDAD DE DESARROLLO ACADEMICO") 

        pdf.setFont("Helvetica-Bold", 8)
        pdf.drawString(245, 750, u"UNIDAD DE PROYECCION SOCIAL")       

    def get_queryset(self, pdf, **kwargs):
        carnet_estudiante = self.kwargs.get('carnet_estudiante')
        queryset = Estudiante.objects.filter(carnet_estudiante = carnet_estudiante)

        for i in Estudiante.objects.filter(carnet_estudiante = carnet_estudiante):
            carnet = i.carnet_estudiante
            nombre = i.nombre_estudiante
            apellido = i.apellido_estudiante
            sexo = i.sexo_estudiante
            telefono = i.telefono_estudiante
            correo = i.correo_estudiante
            direccion = i.direccion_estudiante

        j=0

        for i in Estudiante.objects.all():
            carnetBusqueda = i.carnet_estudiante
            if carnetBusqueda == carnet:
                posicion = j + 1
            else:
                j = j + 1

        numero = posicion

        for i in EstudioUniversitario.objects.filter(carnet_estudiante = carnet_estudiante):
            carrera = i.codigo_carrera.nombre_carrera
            porc_carrera = i.porc_carrerar_aprob
            und_valor = i.unidades_valorativas
            experiencia = i.experiencia_areas_conoc
            ciclo_lect = i.codigo_ciclo

        horas_sem = 5
        dias_sem = 5
        entidad = "Facultad de Agronomia"
        modalidad = "Presencial"
        fecha_inicio = "29/06/2020"
        aceptado = "Si"
        motivo = " "
        observaciones = " "

        # for i in Alumno.objects.filter(codigo_alumno = codigo_alumno):
        #     horas_sem = i.horas_semana
        #     dias_sem = i.dias_semana
        #     entidad = i.propuesta_entidad
        #     modalidad = i.propuesta_modalidad
        #     fecha_inicio = i.fecha_inicio
        #     aceptado = i.estado_expediente
        #     motivo = i.motivo
        #     observaciones = i.observaciones

        texto = 'No. Correlativo: %s' % numero
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(450, 705, texto)

        pdf.setFont("Helvetica-Bold", 26)
        pdf.drawString(100, 720, u"F-1")

        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(235, 710, u"SOLICITUD DE SERVICIO SOCIAL")

        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(60, 690, u"DATOS PERSONALES")

        texto = 'Nombre Completo: %s' % nombre + apellido
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 675, texto)

        #--------------------------------------
        #texto = 'Nombre Completo: ' 
        #pdf.setFont("Helvetica-Bold", 10)
        #pdf.drawString(60, 675, texto)

        #texto = ' %s' % nombre
        #pdf.setFont("Helvetica", 10)
        #pdf.drawString(150, 675, texto)
        #---------------------------------------

        texto = 'Sexo: %s' % sexo
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 660, texto)

        texto = 'Telefono: %s' % telefono
        pdf.setFont("Helvetica", 10)
        pdf.drawString(150, 660, texto)

        texto = 'Correo: %s' % correo
        pdf.setFont("Helvetica", 10)
        pdf.drawString(330, 660, texto)

        texto = 'Direccion Residencial: %s' % direccion
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 645, texto)

        #Agrega una linea horizontal como division
        pdf.line(60, 630, 560, 630)

        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(60, 610, u"ESTUDIO UNIVERSITARIO")

        texto = 'Carrera: %s' % carrera
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 595, texto)

        texto = 'Carnet No.: %s' % carnet
        pdf.setFont("Helvetica", 10)
        pdf.drawString(450, 595, texto)

        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(60, 575, u"Estado Academico:")

        texto = 'Porcentaje de la carrera aprobado: %s' % porc_carrera
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 560, texto)

        texto = 'Unidades Valorativas: %s' % und_valor
        pdf.setFont("Helvetica", 10)
        pdf.drawString(280, 560, texto)

        texto = 'Ciclo Lectivo: %s' % ciclo_lect
        pdf.setFont("Helvetica", 10)
        pdf.drawString(450, 560, texto)

        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 545, u"Experiencia en algunas areas de conocimiento de su carrera: ")

        texto = '%s' % experiencia
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 530, texto)

        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(60, 495, u"Tiempo disponible para su desarrollo social: ")

        texto = 'Horas por Semana: %s' % horas_sem
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 480, texto)

        texto = 'Dias por Semana: %s' % dias_sem
        pdf.setFont("Helvetica", 10)
        pdf.drawString(330, 480, texto)

        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 465, u"Propuesta de la entidad donde realizara su servicio social segun el ambito mencionado en el Manual de ")
        pdf.drawString(60, 450, u"procedimientos del Servicio Social: ")

        texto = '%s' % entidad
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 435, texto)

        #Agrega una linea horizontal como division
        pdf.line(60, 420, 560, 420)

        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 400, u"Propuesta de modalidad de servicio segun las mencionadas en el Manual de Procedimientos del Servicio ")

        texto = 'Social: %s' % modalidad
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 385, texto)

        texto = 'Fecha de Inicio posible: %s' % fecha_inicio
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 370, texto)

        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 335, u"Firma del solicitante: ")
        pdf.line(155, 335, 300, 335)

        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 305, u"Ciudad Universitaria, ")
        pdf.line(155, 305, 200, 305)

        pdf.setFont("Helvetica", 10)
        pdf.drawString(210, 305, u"de")
        pdf.line(230, 305, 320, 305)

        pdf.setFont("Helvetica", 10)
        pdf.drawString(330, 305, u"del ")
        pdf.line(350, 305, 410, 305)

        #Agrega una linea horizontal como division
        pdf.line(60, 285, 560, 285)

        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(60, 265, u"PARA USO EXCLUSIVO DE PROYECCION SOCIAL ")

        texto = 'Aceptado: %s' % aceptado
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 245, texto)

        texto = 'Motivo: %s' % motivo
        pdf.setFont("Helvetica", 10)
        pdf.drawString(200, 245, texto)

        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 225, u"Observaciones: ")

        texto = '%s' % observaciones
        pdf.setFont("Helvetica", 10)
        pdf.drawString(60, 210, texto)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(generarF1, self).get_context_data(**kwargs)
        carnet_estudiante = self.kwargs.get('carnet_estudiante')
        context['carnet_estudiante'] = carnet_estudiante
        return context
         
    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')

        pdf_name = "Comprobante_F1_UPS.pdf"
        # Esta linea es por si deseas descargar el pdf a tu computadora
        response['Content-Disposition'] = 'inline; filename=%s' % pdf_name

        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()

        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)

        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        self.get_queryset(pdf)

        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


# #-----------------------------------------------------------------------------------------------

class generarF8(ListView):
    model = Estudiante
    template_name = 'app1/Estudiante.html'
    context_object_name = 'estudiante'
    success_url = reverse_lazy('proyeccionsocial:generar_F1')  
     
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen1 = 'static/img/logoUPSAgro.png'
        archivo_imagen2 = 'static/img/logoUES.jpg'

        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen1, 50, 730, 125, 90,preserveAspectRatio=True) 
        pdf.drawImage(archivo_imagen2, 430, 720, 125, 90,preserveAspectRatio=True) 

        #Establecemos el tamaño de letra en 8 y el tipo de letra Helvetica en negrita
        #Luego en drawString se colocan las coordenadas X Y de donde se quiere poner
        #el texto, el eje Y inicia en la parte inferior izquierda, ahi es el punto (0, 0)
        pdf.setFont("Helvetica-Bold", 8)
        pdf.drawString(248, 780, u"UNIVERSIDAD DE EL SALVADOR")

        pdf.setFont("Helvetica-Bold", 8)
        pdf.drawString(232, 770, u"FACULTAD DE CIENCIAS AGRONOMICAS")  

        pdf.setFont("Helvetica-Bold", 8)
        pdf.drawString(234, 760, u"UNIDAD DE DESARROLLO ACADEMICO") 

        pdf.setFont("Helvetica-Bold", 8)
        pdf.drawString(245, 750, u"UNIDAD DE PROYECCION SOCIAL")        

    def get_queryset(self, pdf, **kwargs):
        carnet_estudiante = self.kwargs.get('carnet_estudiante')
        queryset = Estudiante.objects.filter(carnet_estudiante = carnet_estudiante)

        for i in Estudiante.objects.filter(carnet_estudiante = carnet_estudiante):
            carnet = i.carnet_estudiante
            nombre = i.nombre_estudiante
            apellido = i.apellido_estudiante
            sexo = i.sexo_estudiante
            telefono = i.telefono_estudiante
            correo = i.correo_estudiante
            direccion = i.direccion_estudiante

        j=0

        for i in Estudiante.objects.all():
            carnetBusqueda = i.carnet_estudiante
            if carnetBusqueda == carnet:
                posicion = j + 1
            else:
                j = j + 1

        numero = posicion

        for i in EstudioUniversitario.objects.filter(carnet_estudiante = carnet_estudiante):
            carrera = i.codigo_carrera.nombre_carrera
            porc_carrera = i.porc_carrerar_aprob
            und_valor = i.unidades_valorativas
            experiencia = i.experiencia_areas_conoc
            ciclo_lect = i.codigo_ciclo

        horas_sem = 5
        dias_sem = 5
        entidad = "Facultad de Agronomia"
        modalidad = "Presencial"
        fecha_inicio = "29/06/2020"
        aceptado = "Si"
        motivo = " "
        observaciones = " "

        # for i in Alumno.objects.filter(codigo_alumno = codigo_alumno):
        #     horas_sem = i.horas_semana
        #     dias_sem = i.dias_semana
        #     entidad = i.propuesta_entidad
        #     modalidad = i.propuesta_modalidad
        #     fecha_inicio = i.fecha_inicio
        #     aceptado = i.estado_expediente
        #     motivo = i.motivo
        #     observaciones = i.observaciones

        pdf.setFont("Helvetica-Bold", 26)
        pdf.drawString(100, 720, u"F-8")

        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(60, 690, u"HOJA DE REGISTRO DE LAS HORAS SOCIALES REALIZADAS EN LA ESTACIÓN EXPERIMENTAL Y DE")
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(180, 675, u"PRÁCTICAS POR ESTUDIANTES DE LA UNIVERSIDAD")

        #texto = 'Nombre Completo: %s' % nombre + apellido
        #pdf.setFont("Helvetica", 10)
        #pdf.drawString(60, 675, texto)

        #--------------------------------------
        #texto = 'Nombre Completo: ' 
        #pdf.setFont("Helvetica-Bold", 10)
        #pdf.drawString(60, 675, texto)

        #texto = ' %s' % nombre
        #pdf.setFont("Helvetica", 10)
        #pdf.drawString(150, 675, texto)
        #---------------------------------------

        #texto = 'Sexo: %s' % sexo
        #pdf.setFont("Helvetica", 10)
        #pdf.drawString(60, 660, texto)

        #texto = 'Telefono: %s' % telefono
        #pdf.setFont("Helvetica", 10)
        #pdf.drawString(150, 660, texto)

        #texto = 'Correo: %s' % correo
        #pdf.setFont("Helvetica", 10)
        #pdf.drawString(330, 660, texto)

        #texto = 'Direccion Residencial: %s' % direccion
        #pdf.setFont("Helvetica", 10)
        #pdf.drawString(60, 645, texto)

        #Agrega una linea horizontal como division
        # pdf.line(60, 630, 560, 630)

        # pdf.setFont("Helvetica-Bold", 10)
        # pdf.drawString(60, 610, u"ESTUDIO UNIVERSITARIO")

        # texto = 'Carrera: %s' % carrera
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 595, texto)

        # texto = 'Carnet No.: %s' % carnet
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(450, 595, texto)

        # pdf.setFont("Helvetica-Bold", 10)
        # pdf.drawString(60, 575, u"Estado Academico:")

        # texto = 'Porcentaje de la carrera aprobado: %s' % porc_carrera
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 560, texto)

        # texto = 'Unidades Valorativas: %s' % und_valor
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(280, 560, texto)

        # texto = 'Ciclo Lectivo: %s' % ciclo_lect
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(450, 560, texto)

        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 545, u"Experiencia en algunas areas de conocimiento de su carrera: ")

        # texto = '%s' % experiencia
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 530, texto)

        # pdf.setFont("Helvetica-Bold", 10)
        # pdf.drawString(60, 495, u"Tiempo disponible para su desarrollo social: ")

        # texto = 'Horas por Semana: %s' % horas_sem
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 480, texto)

        # texto = 'Dias por Semana: %s' % dias_sem
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(330, 480, texto)

        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 465, u"Propuesta de la entidad donde realizara su servicio social segun el ambito mencionado en el Manual de ")
        # pdf.drawString(60, 450, u"procedimientos del Servicio Social: ")

        # texto = '%s' % entidad
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 435, texto)

        # #Agrega una linea horizontal como division
        # pdf.line(60, 420, 560, 420)

        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 400, u"Propuesta de modalidad de servicio segun las mencionadas en el Manual de Procedimientos del Servicio ")

        # texto = 'Social: %s' % modalidad
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 385, texto)

        # texto = 'Fecha de Inicio posible: %s' % fecha_inicio
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 370, texto)

        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 335, u"Firma del solicitante: ")
        # pdf.line(155, 335, 300, 335)

        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 305, u"Ciudad Universitaria, ")
        # pdf.line(155, 305, 200, 305)

        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(210, 305, u"de")
        # pdf.line(230, 305, 320, 305)

        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(330, 305, u"del ")
        # pdf.line(350, 305, 410, 305)

        # #Agrega una linea horizontal como division
        # pdf.line(60, 285, 560, 285)

        # pdf.setFont("Helvetica-Bold", 10)
        # pdf.drawString(60, 265, u"PARA USO EXCLUSIVO DE PROYECCION SOCIAL ")

        # texto = 'Aceptado: %s' % aceptado
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 245, texto)

        # texto = 'Motivo: %s' % motivo
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(200, 245, texto)

        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 225, u"Observaciones: ")

        # texto = '%s' % observaciones
        # pdf.setFont("Helvetica", 10)
        # pdf.drawString(60, 210, texto)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(generarF1, self).get_context_data(**kwargs)
        carnet_estudiante = self.kwargs.get('carnet_estudiante')
        context['carnet_estudiante'] = carnet_estudiante
        return context
         
    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')

        pdf_name = "Comprobante_F8_UPS.pdf"
        # Esta linea es por si deseas descargar el pdf a tu computadora
        response['Content-Disposition'] = 'inline; filename=%s' % pdf_name

        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()

        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)

        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        self.get_queryset(pdf)

        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response