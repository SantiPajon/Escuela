from django.urls import path
from Clase.views import index, estudiante_list, estudiante_create, profesor_create, profesor_list,principal_profesores,principal_cursos,curso_create,curso_list

app_name = "Clase"

urlpatterns = [
    path("", index, name="index"),
    path("Clase/list", estudiante_list,name="estudiante_list" ),
    path("Clase/create", estudiante_create,name="estudiante_create" ),
    path("principal_profesores", principal_profesores,name="principal_profesores" ),
    path("profesor_list", profesor_list,name="profesor_list" ),
    path("profesor_create", profesor_create,name="profesor_create" ),
    path("principal_cursos", principal_cursos,name="principal_cursos" ),
    path("curso_create", curso_create,name="curso_create" ),
    path("curso_list", curso_list,name="curso_list" ),
]
