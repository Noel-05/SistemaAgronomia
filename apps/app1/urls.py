from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required


app_name='proyeccionsocial'

urlpatterns=[
	#URL para el menu de inicio
	path('', index),
	path('proyeccionsocial/index/',index, name='index'),

	#URL para Estudiante
	path('proyeccionsocial/consultaEstudiante/',login_required(consultaEstudiante), name="consulta_estudiante"),
	path('proyeccionsocial/crearEstudiante/',login_required(crearEstudiante.as_view()), name="crear_estudiante"),
	path('proyeccionsocial/editarEstudiante/<pk>/',login_required(editarEstudiante.as_view()), name="editar_estudiante"),
	path('proyeccionsocial/eliminarEstudiante/<pk>/',login_required(eliminarEstudiante.as_view()), name="eliminar_estudiante"),
	#Buscar Estudiante
	path('proyeccionsocial/consultaEstudianteBuscar',consultaEstudianteBuscar, name="consulta_estudiante_buscar"),


	#URL para Ciclo
	path('proyeccionsocial/consultaCiclo/',login_required(consultaCiclo), name="consulta_ciclo"),
	path('proyeccionsocial/crearCiclo/',login_required(crearCiclo.as_view()), name="crear_ciclo"),
	path('proyeccionsocial/editarCiclo/<pk>/',login_required(editarCiclo.as_view()), name="editar_ciclo"),
	path('proyeccionsocial/eliminarCiclo/<pk>/',login_required(eliminarCiclo.as_view()), name="eliminar_ciclo"),


	#URL para Estudio Universitario
	path('proyeccionsocial/consultaEstudioUniversitario/',login_required(consultaEstudioUniversitario), name="consulta_estudio_universitario"),
	path('proyeccionsocial/crearEstudioUniversitario/',login_required(crearEstudioUniversitario.as_view()), name="crear_estudio_universitario"),
	path('proyeccionsocial/editarEstudioUniversitario/<pk>/',login_required(editarEstudioUniversitario.as_view()), name="editar_estudio_universitario"),
	path('proyeccionsocial/eliminarEstudioUniversitario/<pk>/',login_required(eliminarEstudioUniversitario.as_view()), name="eliminar_estudio_universitario"),


	#URL para la Solicitud de Servicio Social
	path('proyeccionsocial/consultaSolicitudServicioSocial/',login_required(consultaSolicitudServicioSocial), name="consulta_solicitud_servicio_social"),
	path('proyeccionsocial/crearSolicitudServicioSocial/',login_required(crearSolicitudServicioSocial.as_view()), name="crear_solicitud_servicio_social"),
	path('proyeccionsocial/editarSolicitudServicioSocial/<pk>/',login_required(editarSolicitudServicioSocial.as_view()), name="editar_solicitud_servicio_social"),
	path('proyeccionsocial/eliminarSolicitudServicioSocial/<pk>/',login_required(eliminarSolicitudServicioSocial.as_view()), name="eliminar_solicitud_servicio_social"),


	#URL para el Estado de la Solicitud de Servicio Social
	path('proyeccionsocial/consultaEstadoSolicitudServicioSocial/',login_required(consultaEstadoSolicitudServicioSocial), name="consulta_estado_solicitud_servicio_social"),
	path('proyeccionsocial/crearEstadoSolicitudServicioSocial/',login_required(crearEstadoSolicitudServicioSocial.as_view()), name="crear_estado_solicitud_servicio_social"),
	path('proyeccionsocial/editarEstadoSolicitudServicioSocial/<pk>/',login_required(editarEstadoSolicitudServicioSocial.as_view()), name="editar_estado_solicitud_servicio_social"),
	path('proyeccionsocial/eliminarEstadoSolicitudServicioSocial/<pk>/',login_required(eliminarEstadoSolicitudServicioSocial.as_view()), name="eliminar_estado_solicitud_servicio_social"),


	#URL para los Formularios
	path('proyeccionsocial/generarF1/<str:carnet_estudiante>/',login_required(generarF1.as_view()), name= "generar_F1"),
	path('proyeccionsocial/generarF2/<str:carnet_estudiante>/',login_required(generarF2.as_view()), name= "generar_F2"),
	path('proyeccionsocial/generarF3/<str:carnet_estudiante>/',login_required(generarF3.as_view()), name= "generar_F3"),
	path('proyeccionsocial/generarF4TI/<str:carnet_estudiante>/',login_required(generarF4TI.as_view()), name= "generar_F4TI"),
	path('proyeccionsocial/generarF4TE/<str:carnet_estudiante>/',login_required(generarF4TE.as_view()), name= "generar_F4TE"),
	path('proyeccionsocial/generarF6/<str:carnet_estudiante>/',login_required(generarF6.as_view()), name= "generar_F6"),
	path('proyeccionsocial/generarF7/<str:carnet_estudiante>/',login_required(generarF7.as_view()), name= "generar_F7"),
	path('proyeccionsocial/generarF8/<str:carnet_estudiante>/',login_required(generarF8.as_view()), name= "generar_F8"),
	path('proyeccionsocial/generarF9/<str:carnet_estudiante>/',login_required(generarF9.as_view()), name= "generar_F9"),
	path('proyeccionsocial/generarF11/<str:carnet_estudiante>/',login_required(generarF11.as_view()), name= "generar_F11"),
]