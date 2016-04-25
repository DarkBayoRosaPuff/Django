from django.contrib import admin

# Register your models here.
from Modelos.models import Genero
admin.site.register(Genero)

from Modelos.models import Entidad
admin.site.register(Entidad)

from Modelos.models import Publicacion
admin.site.register(Publicacion)

from Modelos.models import Album
admin.site.register(Album)