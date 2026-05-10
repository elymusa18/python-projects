from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.insecure_login, name="insecure_login"),
    path("search/", views.insecure_search, name="insecure_search"),

    path("login-safe/", views.safe_login, name="safe_login"),
    path("search-safe/", views.safe_search, name="safe_search"),
]