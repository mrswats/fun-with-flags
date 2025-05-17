from django.http import HttpRequest
from django.http import JsonResponse


def healthcheck(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})
