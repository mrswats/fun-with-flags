from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include("fun_with_flags.healthcheck.urls")),
    path("admin/", admin.site.urls),
]
