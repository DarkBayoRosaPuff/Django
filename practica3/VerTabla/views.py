from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from Modelos.models import Genero
from Modelos.models import Entidad

# Create your views here.
# Muestra la tabla de generos
def consultarGeneros(request):
	contenido = Genero.objects.all().order_by('nombre')
	plantilla = loader.get_template('generos.html')
	if request.user.is_authenticated():
		usuarioActual = request.user;
	else:
		usuarioActual = None;
	contexto = {
	'contenido': contenido,
	'usuarioActual': usuarioActual,
	}
	return HttpResponse(plantilla.render(contexto,request))
# Muestra la tabla de entidades musicales
def consultarEntidades(request):
	contenido = Entidad.objects.all().order_by('nombre')
	generos = Genero.objects.all()
	plantilla = loader.get_template('entidades.html')
	if request.user.is_authenticated():
		usuarioActual = request.user;
	else:
		usuarioActual = None;
	contexto = {
	'contenido': contenido,
	'usuarioActual': usuarioActual,
	'generos': generos,
	}
	return HttpResponse(plantilla.render(contexto,request))

# Agrega una nueva tupla a la tabla Genero
def agregarGenero(request):
	nuevo = Genero(nombre = request.POST['nombre'])
	nuevo.save()
	return consultarGeneros(request)
# Agrega una nueva tupla a la tabla Entidad
def agregarEntidad(request):
	nuevo = Entidad(nombre = request.POST['nombre'], fechaInicio = request.POST['fechaInicio'], genero = request.POST['genero'])
	nuevo.save()
	return consultarEntidades(request)