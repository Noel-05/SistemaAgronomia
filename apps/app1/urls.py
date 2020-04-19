from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required


app_name='proyeccionsocial'

urlpatterns=[
	#URL para el menu de inicio
	path('', index),
	path('proyeccionsocial/index/',index, name='index'),

	#URL para Alumno
	path('proyeccionsocial/consultaAlumno/',consultaAlumno, name="consulta_alumno"),
	path('proyeccionsocial/crearAlumno/',crearAlumno.as_view(), name="crear_alumno"),
	path('proyeccionsocial/editarAlumno/<pk>/',editarAlumno.as_view(), name="editar_alumno"),
	path('proyeccionsocial/eliminarAlumno/<pk>/',eliminarAlumno.as_view(), name="eliminar_alumno"),

	#URL para Alumno
	path('proyeccionsocial/consultaCiclo/',consultaCiclo, name="consulta_ciclo"),
	path('proyeccionsocial/crearCiclo/',crearCiclo.as_view(), name="crear_ciclo"),
	path('proyeccionsocial/editarCiclo/<pk>/',editarCiclo.as_view(), name="editar_ciclo"),
	path('proyeccionsocial/eliminarCiclo/<pk>/',eliminarCiclo.as_view(), name="eliminar_ciclo"),

	path('proyeccionsocial/generarpdf/<int:codigo_alumno>/',generarpdf.as_view(), name= "generar_pdf"),
]