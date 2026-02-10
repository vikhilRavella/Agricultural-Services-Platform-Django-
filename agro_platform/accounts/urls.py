from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CustomLoginView, demo_login

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("demo/", demo_login, name="demo_login"),
]
