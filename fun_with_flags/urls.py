from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("", include("fun_with_flags.healthcheck.urls")),
    path("admin/", admin.site.urls),
]
