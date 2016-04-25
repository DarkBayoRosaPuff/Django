from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^consultarGeneros/$', views.consultarGeneros, name='consultarGeneros'),
    url(r'^agregarGenero/$', views.agregarGenero, name='agregarGenero'),

    url(r'^consultarEntidades/$', views.consultarEntidades, name='consultarEntidades'),
    url(r'^agregarEntidad/$', views.agregarEntidad, name='agregarEntidad'),
]