from django.shortcuts import render, redirect
from .models import Estudiante,Profesor
from Clase.forms import EstudianteForm,ProfesorForm
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

def profesor_create(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:principal_profesores")
        
    else: #GET
        form = ProfesorForm()
    return render(request, "Clase/profesor_create.html",{"form":form})

def profesor_list(request):
    consulta = Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request,"Clase/profesor_list.html", contexto)

def principal_profesores(request):
    return render(request,"Clase/principal_profesores.html")