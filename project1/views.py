from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Juan Carlos")

def segunda_vista(request):
    return HttpResponse("<br><br><br><h1>AGUANTE LINUX LA CONCHA DE MI HERMANA</h1> ")

def diaDeHoy(request):
    
    dia = datetime.now()

    documentoDeTexto = f"<h1>Hoy es <br> {dia}<h1>"

    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):

    documentoDeTexto = f"Mi nombre es <br><br> {nombre}"

    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):

    miHtml = open('/home/z0skia/curso_python/django_proyect/project1/project1/project1/plantillas/template1.html')

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

    
