from django.urls import path
from . import views
from core.views import register
from core.views import CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/",CustomLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(template_name="core/logout.html"),name="logout"),
    path("register/",register, name="register")
]
