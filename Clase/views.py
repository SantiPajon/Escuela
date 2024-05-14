from django.shortcuts import render, redirect
from .models import Estudiante
from Clase.forms import EstudianteForm
# Create your views here.

def index(request):
    return render(request,"Clase/index.html")

def estudiante_list(request):
    consulta = Estudiante.objects.all()
    contexto = {"estudiantes": consulta}
    return render(request,"Clase/estudiante_list.html", contexto)

def estudiante_create(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:index")
        
    else: #GET
        form = EstudianteForm()
    return render(request, "Clase/estudiante_create.html",{"form":form})