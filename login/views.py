from django.shortcuts import render


def login(request):
    return render(request, "login/pages/login.html")
