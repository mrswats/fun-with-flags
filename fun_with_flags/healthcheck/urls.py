from django.urls import path

from fun_with_flags.healthcheck.views import healthcheck


urlpatterns = [
    path("healthcheck/", healthcheck, name="healthcheck"),
]
