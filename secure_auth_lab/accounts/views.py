from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .models import VulnerableUser, SafeUser


def home_view(request):
    vulnerable_username = request.session.get("vulnerable_username")
    safe_username = request.session.get("safe_username")

    context = {
        "vulnerable_username": vulnerable_username,
        "safe_username": safe_username,
    }
    return render(request, "accounts/home.html", context)



def vulnerable_register(request):
    error = ""
    success = ""

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            error = "Всички полета са задължителни."
        elif VulnerableUser.objects.filter(username=username).exists():
            error = "Потребителското име вече съществува."
        else:
            VulnerableUser.objects.create(
                username=username,
                password=password
            )
            success = "Регистрацията е успешна. Паролата е записана в plaintext."

    return render(request, "accounts/vulnerable_register.html", {
        "error": error,
        "success": success
    })


def vulnerable_login(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        try:
            user = VulnerableUser.objects.get(username=username)
            if user.password == password:
                request.session["vulnerable_username"] = user.username
                return redirect("home")
            else:
                error = "Невалидно потребителско име или парола."
        except VulnerableUser.DoesNotExist:
            error = "Невалидно потребителско име или парола."

    return render(request, "accounts/vulnerable_login.html", {
        "error": error
    })


def vulnerable_logout(request):
    request.session.pop("vulnerable_username", None)
    return redirect("home")


def vulnerable_users_list(request):
    users = VulnerableUser.objects.all().order_by("id")
    return render(request, "accounts/vulnerable_users_list.html", {
        "users": users
    })


def safe_register(request):
    error = ""
    success = ""

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            error = "Всички полета са задължителни."
        elif SafeUser.objects.filter(username=username).exists():
            error = "Потребителското име вече съществува."
        else:
            SafeUser.objects.create(
                username=username,
                password=make_password(password)
            )
            success = "Регистрацията е успешна. Паролата е записана хеширана."

    return render(request, "accounts/safe_register.html", {
        "error": error,
        "success": success
    })


def safe_login(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        try:
            user = SafeUser.objects.get(username=username)
            if check_password(password, user.password):
                request.session["safe_username"] = user.username
                return redirect("home")
            else:
                error = "Невалидно потребителско име или парола."
        except SafeUser.DoesNotExist:
            error = "Невалидно потребителско име или парола."

    return render(request, "accounts/safe_login.html", {
        "error": error
    })


def safe_logout(request):
    request.session.pop("safe_username", None)
    return redirect("home")


def safe_users_list(request):
    users = SafeUser.objects.all().order_by("id")
    return render(request, "accounts/safe_users_list.html", {
        "users": users
    })