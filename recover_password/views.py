from django.shortcuts import render


def recover_password(request):
    return render(request, "recover_password/pages/recover-password.html")
