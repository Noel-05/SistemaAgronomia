from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required


app_name='proyeccionsocial'

urlpatterns=[
	#URL para el menu de inicio
	path('', index),
	path('proyeccionsocial/index/',index, name='index'),

	#URL para Alumno
	path('proyeccionsocial/consultaEstudiante/',consultaEstudiante, name="consulta_estudiante"),
	path('proyeccionsocial/crearEstudiante/',crearEstudiante.as_view(), name="crear_estudiante"),
	path('proyeccionsocial/editarEstudiante/<pk>/',editarEstudiante.as_view(), name="editar_estudiante"),
	path('proyeccionsocial/eliminarEstudiante/<pk>/',eliminarEstudiante.as_view(), name="eliminar_estudiante"),

	#URL para Alumno
	path('proyeccionsocial/consultaCiclo/',consultaCiclo, name="consulta_ciclo"),
	path('proyeccionsocial/crearCiclo/',crearCiclo.as_view(), name="crear_ciclo"),
	path('proyeccionsocial/editarCiclo/<pk>/',editarCiclo.as_view(), name="editar_ciclo"),
	path('proyeccionsocial/eliminarCiclo/<pk>/',eliminarCiclo.as_view(), name="eliminar_ciclo"),

	#URL para Estudio Universitario
	path('proyeccionsocial/consultaEstudioUniversitario/',consultaEstudioUniversitario, name="consulta_estudio_universitario"),
	path('proyeccionsocial/crearEstudioUniversitario/', crearEstudioUniversitario.as_view(), name="crear_estudio_universitario"),
	path('proyeccionsocial/editarEstudioUniversitario/<pk>/',editarEstudioUniversitario.as_view(), name="editar_estudio_universitario"),
	path('proyeccionsocial/eliminarEstudioUniversitario/<pk>/',eliminarEstudioUniversitario.as_view(), name="eliminar_estudio_universitario"),

	#URL para la Solicitud de Servicio Social
	path('proyeccionsocial/consultaSolicitudServicioSocial/',consultaSolicitudServicioSocial, name="consulta_solicitud_servicio_social"),
	path('proyeccionsocial/crearSolicitudServicioSocial/', crearSolicitudServicioSocial.as_view(), name="crear_solicitud_servicio_social"),
	path('proyeccionsocial/editarSolicitudServicioSocial/<pk>/',editarSolicitudServicioSocial.as_view(), name="editar_solicitud_servicio_social"),
	path('proyeccionsocial/eliminarSolicitudServicioSocial/<pk>/',eliminarSolicitudServicioSocial.as_view(), name="eliminar_solicitud_servicio_social"),

	#URL para los Formularios
	path('proyeccionsocial/generarF1/<str:carnet_estudiante>/',generarF1.as_view(), name= "generar_F1"),
	path('proyeccionsocial/generarF7/<str:carnet_estudiante>/',generarF7.as_view(), name= "generar_F7"),
	path('proyeccionsocial/generarF8/<str:carnet_estudiante>/',generarF8.as_view(), name= "generar_F8"),
	path('proyeccionsocial/generarF9/<str:carnet_estudiante>/',generarF9.as_view(), name= "generar_F9"),
]