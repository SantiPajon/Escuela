from django.urls import path
from Clase.views import index, estudiante_list, estudiante_create

app_name = "Clase"

urlpatterns = [
    path("", index, name="index"),
    path("Clase/list", estudiante_list,name="estudiante_list" ),
    path("Clase/create", estudiante_create,name="estudiante_create" ),
]
