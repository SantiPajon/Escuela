from django.shortcuts import render
from .models import Estudiante
# Create your views here.

def index(request):
    return render(request,"Clase/index.html")

def estudiante_list(request):
    consulta = Estudiante.objects.all()
    contexto = {"estudiantes": consulta}
    return render(request,"Clase/estudiante_list.html", contexto)