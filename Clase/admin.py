from django.contrib import admin
from .models import Curso,Estudiante,Profesor

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
