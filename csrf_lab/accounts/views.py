from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def home_view(request):
    return render(request, "accounts/home.html")


def user_login(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("profile")
        else:
            error = "Invalid credentials"

    return render(request, "accounts/login.html", {"error": error})


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")