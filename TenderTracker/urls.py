from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


def custom_root_redirect(request):
    if request.user.is_authenticated:
        return redirect("tenders:tender-list")
    else:
        return redirect("login")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tenders/", include("tenders.urls", namespace="tenders")),
    path("auth/", include("django.contrib.auth.urls")),
    path("", custom_root_redirect, name="root"),
]
