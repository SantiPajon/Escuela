from django.urls import path
from Clase.views import index, estudiante_list

app_name = "Clase"

urlpatterns = [
    path("", index, name="index"),
    path("Clase/list", estudiante_list,name="estudiante_list" )
]
