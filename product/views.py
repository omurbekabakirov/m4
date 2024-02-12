from django.shortcuts import render
from django.http import HttpResponse
from datetime import  datetime


def hello_view(request):
    return HttpResponse("Hello ! it's my project")


def current_date_view(request):
    time = datetime.now()
    return HttpResponse(time)


def goodbye_view(request):
    return HttpResponse("Goodbye user !")
