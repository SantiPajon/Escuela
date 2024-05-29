from django.urls import path
from Clase.views import (
    index, estudiante_list,
    estudiante_create,
    profesor_create,
    profesor_list,
    principal_profesores,
    principal_cursos,
    curso_create,
    curso_list,
    CursoDetail,
    CursoDelete,
    CursoUpdate,
    EstudianteDelete,
    ProfesorDelete,
    ProfesorUpdate,
    ProfesorCreate)

app_name = "Clase"

urlpatterns = [
    path("", index, name="index"),
    path("Clase/list", estudiante_list,name="estudiante_list" ),
    path("Clase/create", estudiante_create,name="estudiante_create" ),
    path("principal_profesores", principal_profesores,name="principal_profesores" ),
    path("profesor_list", profesor_list,name="profesor_list" ),
    path("principal_cursos", principal_cursos,name="principal_cursos" ),
    path("curso_create", curso_create,name="curso_create" ),
    path("curso_list", curso_list,name="curso_list" ),
    path("curso/detail/<int:pk>", CursoDetail.as_view(), name="curso_detail"),
    path("curso/delete/<int:pk>", CursoDelete.as_view(), name="curso_delete"),
    path("curso/update/<int:pk>", CursoUpdate.as_view(), name="curso_update"),
    path("estudiante/delete/<int:pk>", EstudianteDelete.as_view(), name="estudiante_delete"),
    path("profesor/delete/<int:pk>", ProfesorDelete.as_view(), name="profesor_delete"),
    path("profesor/update/<int:pk>", ProfesorUpdate.as_view(), name="profesor_update"),
    path("profesor/create", ProfesorCreate.as_view(), name="profesor_create"),
]
