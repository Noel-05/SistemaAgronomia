from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

app_name='proyeccionsocial'

urlpatterns=[
	#URL para el menu de inicio
	path('', index),
	path('proyeccionsocial/index/',index, name='index'),

	#URL para la consulta de Expediente
	path('proyeccionsocial/consultaexpediente/',consultaexpediente, name="consulta_expediente"),
    path('proyeccionsocial/agregarexpediente/',agregarExpediente.as_view(), name='agregar_expediente'),

	path('proyeccionsocial/generarpdf/',generarpdf.as_view(), name= "generar_pdf"),
]