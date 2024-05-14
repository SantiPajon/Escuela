from django.urls import path
from . import views

app_name = "Clase"

urlpatterns = [
    path("", views.index, name="index"),
]
