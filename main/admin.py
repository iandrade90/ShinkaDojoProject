from django.contrib import admin
from .models import (
        Inicio,
        Acerca,
        Programa,
        Contacto,
        PresentacionEstilos,
        Estilo
        )

admin.site.register(Inicio)
admin.site.register(Acerca)
admin.site.register(Programa)
admin.site.register(Contacto)
admin.site.register(PresentacionEstilos)
admin.site.register(Estilo)
