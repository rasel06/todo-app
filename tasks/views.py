from django.shortcuts import render
from django.http import (JsonResponse)

# Create your views here.


def index(request):
    response = {
        "message": "Only Get Request Support",
        "code": 400
    }
    if request.method == "GET":
        response['message'] = "Success"
        response['code'] = 200
        response['data'] = []
        return JsonResponse(response, safe=False)
    else:
        return JsonResponse(response, safe=False)
