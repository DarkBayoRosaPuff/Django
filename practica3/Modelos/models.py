from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.

class Entidad(models.Model):
	nombre = models.CharField(max_length=200);
	fechaInicio = models.DateField();
	genero = models.CharField(max_length=100);

	def __str__(self):
		return "%s" % (self.nombre)

class Genero(models.Model):
	nombre = models.CharField(max_length=100);

class Publicacion(models.Model):
	titulo = models.CharField(max_length = 100);
	cuerpo = models.CharField(max_length=200);
	fechaInicio = models.DateTimeField(auto_now_add=True, blank=True);
	entidadID = models.ForeignKey(Entidad, on_delete=models.CASCADE);

class Album(models.Model):
	nombre = models.CharField(max_length=200);
	entidadID = models.ForeignKey(Entidad, on_delete=models.CASCADE);