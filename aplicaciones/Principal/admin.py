from django.contrib import admin
from .models import *

admin.site.register(paciente)
admin.site.register(tratamiento)
admin.site.register(areaTratamiento)
admin.site.register(historial)

