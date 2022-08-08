from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("login.urls")),
    path("change-password/", include("change_password.urls")),
    path("recover-password/", include("recover_password.urls")),
    path("create-user/", include("create_user.urls")),
]
