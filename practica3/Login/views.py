from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from Modelos.models import Album
from Modelos.models import Entidad
from Modelos.models import Publicacion

# Create your views here.
def iniciarSesion(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)

	if user is not None: # Sesion iniciada correctamente
		login(request,user) # Usuario actual agregado a la sesion
	
	formulario = UserCreationForm()
	catalogo = Entidad.objects.all().order_by('nombre')
	publicaciones = Publicacion.objects.all().order_by('-fechaInicio')
	if request.user.is_authenticated():
		usuarioActual = request.user;
	else:
		usuarioActual = None;
	plantilla = loader.get_template('nuevoUsuario.html')
	contexto = {
	'formulario': formulario,
	'catalogo': catalogo,
	'publicaciones': publicaciones,
	'usuarioActual': usuarioActual,
	}
	return HttpResponse(plantilla.render(contexto,request))

def cerrarSesion(request):
	logout(request)
	formulario = UserCreationForm()
	catalogo = Entidad.objects.all().order_by('nombre')
	publicaciones = Publicacion.objects.all().order_by('-fechaInicio')
	if request.user.is_authenticated():
		usuarioActual = request.user;
	else:
		usuarioActual = None;
	plantilla = loader.get_template('nuevoUsuario.html')
	contexto = {
	'formulario': formulario,
	'catalogo': catalogo,
	'publicaciones': publicaciones,
	'usuarioActual': usuarioActual,
	}
	return HttpResponse(plantilla.render(contexto,request))

def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()

	catalogo = Entidad.objects.all().order_by('nombre')
	publicaciones = Publicacion.objects.all().order_by('-fechaInicio')
	if request.user.is_authenticated():
		usuarioActual = request.user;
	else:
		usuarioActual = None;
	return render(request, 'nuevoUsuario.html', {'formulario':formulario, 'catalogo':catalogo, 'publicaciones':publicaciones, 'usuarioActual':usuarioActual})

def agregarAlbum(request):
	nuevo = Album(nombre = request.POST['nombre'],entidadID = Entidad.objects.filter(nombre = request.POST['grupo'] )[0])
	nuevo.save()
	formulario = UserCreationForm()
	catalogo = Entidad.objects.all().order_by('nombre')
	publicaciones = Publicacion.objects.all().order_by('-fechaInicio')
	if request.user.is_authenticated():
		usuarioActual = request.user;
	else:
		usuarioActual = None;
	plantilla = loader.get_template('nuevoUsuario.html')
	contexto = {
	'formulario': formulario,
	'catalogo': catalogo,
	'publicaciones': publicaciones,
	'usuarioActual': usuarioActual,
	}
	return HttpResponse(plantilla.render(contexto,request))

def agregarPublicacion(request):
	nuevo = Publicacion(titulo=request.POST['titulo'],cuerpo=request.POST['cuerpo'],entidadID=Entidad.objects.filter(nombre = request.POST['grupo'])[0])
	nuevo.save()
	formulario = UserCreationForm()
	catalogo = Entidad.objects.all().order_by('nombre')
	publicaciones = Publicacion.objects.all().order_by('-fechaInicio')
	plantilla = loader.get_template('nuevoUsuario.html')
	if request.user.is_authenticated():
		usuarioActual = request.user;
	else:
		usuarioActual = None;
	contexto = {
	'formulario': formulario,
	'catalogo': catalogo,
	'publicaciones': publicaciones,
	'usuarioActual': usuarioActual,
	}
	return HttpResponse(plantilla.render(contexto,request))