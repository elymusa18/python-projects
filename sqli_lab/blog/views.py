from django.shortcuts import render
from django.db import connection
from .models import Post

def home(request):
    return render(request, "home.html")


def insecure_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        query = f"""
        SELECT id, username FROM blog_author
        WHERE username = '{username}'
        AND password = '{password}'
        """
        print(query)
        with connection.cursor() as cursor:
            cursor.execute(query)
            user = cursor.fetchone()

        if user:
            return render(request, "success.html", {"user": user})

        return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def insecure_search(request):
    title = request.GET.get("title", "")

    query = f"SELECT id, title, content FROM blog_post WHERE title = '{title}'"

    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    return render(request, "results.html", {"results": results, "title": title})


def safe_login(request):

    if request.method == "POST":

        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, username FROM blog_author WHERE username = %s AND password = %s",
                [username, password]
            )

            user = cursor.fetchone()

        if user:
            return render(request, "success.html", {"user": user})

        return render(request, "login_safe.html", {"error": "Invalid credentials"})

    return render(request, "login_safe.html")


def safe_search(request):

    title = request.GET.get("title", "")

    results = Post.objects.filter(title=title).values_list("id", "title", "content")

    return render(request, "results_safe.html", {"results": list(results), "title": title})