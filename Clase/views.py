from django.shortcuts import render, redirect
from .models import Estudiante,Profesor,Curso
from Clase.forms import EstudianteForm,ProfesorForm,CursoForm
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request,"Clase/index.html")

def estudiante_list(request):
    busqueda = request.GET.get("busqueda",None)
    if busqueda:
        print(busqueda)
        consulta = Estudiante.objects.filter(nombre__icontains=busqueda)
    else: 
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
    busqueda = request.GET.get("busqueda",None)
    if busqueda:
        print(busqueda)
        consulta = Profesor.objects.filter(nombre__icontains=busqueda)
    else:
       consulta = Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request,"Clase/profesor_list.html", contexto)

def principal_profesores(request):
    return render(request,"Clase/principal_profesores.html")

def principal_cursos(request):
    return render(request,"Clase/principal_cursos.html")

def curso_create(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:principal_cursos")
        
    else: #GET
        form = CursoForm()
    return render(request, "Clase/curso_create.html",{"form":form})


def curso_list(request):
    busqueda = request.GET.get("busqueda",None)
    if busqueda:
        print(busqueda)
        consulta = Curso.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Curso.objects.all()
    contexto = {"cursos": consulta}
    return render(request,"Clase/curso_list.html", contexto)


class CursoDetail(DetailView):
    model = Curso


class CursoDelete(DeleteView):
    model = Curso
    success_url = reverse_lazy("Clase:curso_list")
    
    
class CursoUpdate(UpdateView):
    model = Curso
    form_class = CursoForm
    success_url = reverse_lazy("Clase:curso_list")
    
class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy("Clase:estudiante_list")
    
class ProfesorDelete(DeleteView):
    model = Profesor
    success_url = reverse_lazy("Clase:profesor_list")
    
