import random

from django.http import HttpRequest, HttpResponse, JsonResponse
from time import time


def get_latest_donate(request: HttpRequest) -> HttpResponse:
    timestamp = request.GET.get("timestamp")
    if not timestamp or timestamp == "0":
        return JsonResponse({"answer":
                             [{"nick": "test" + str(random.randint(1, 99999)),
                               "item": "крутой меч"} for _ in range(10)]})
    return JsonResponse({"answer": [{"nick": "test" + str(random.randint(1, 99999)), "item": "крутой меч"}]})
