from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),

    path("vulnerable/register/", views.vulnerable_register, name="vulnerable_register"),
    path("vulnerable/login/", views.vulnerable_login, name="vulnerable_login"),
    path("vulnerable/logout/", views.vulnerable_logout, name="vulnerable_logout"),
    path("vulnerable/users/", views.vulnerable_users_list, name="vulnerable_users_list"),

    path("safe/register/", views.safe_register, name="safe_register"),
    path("safe/login/", views.safe_login, name="safe_login"),
    path("safe/logout/", views.safe_logout, name="safe_logout"),
    path("safe/users/", views.safe_users_list, name="safe_users_list"),
]