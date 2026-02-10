from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from accounts.views import CustomLoginView, demo_login
from dashboard.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("demo/", demo_login, name="demo_login"),
    path("dashboard/", include("dashboard.urls")),
    path("services/", include("services.urls")),
    path("suppliers/", include("suppliers.urls")),
]
