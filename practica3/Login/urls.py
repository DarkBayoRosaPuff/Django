from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.nuevo_usuario, name='nuevo'),
	url(r'^iniciarSesion$', views.iniciarSesion, name='iniciarSesion'),
	url(r'^cerrarSesion$', views.cerrarSesion, name='logout'),
	url(r'^nuevo_usuario$', views.nuevo_usuario, name='nuevo_usuario'),
	url(r'^agregarAlbum$', views.agregarAlbum, name='agregarAlbum'),
	url(r'^agregarPublicacion$', views.agregarPublicacion, name='agregarPublicacion'),
]