from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from product.models import Product


def hello_view(request):
    return HttpResponse("Hello ! it's my project")


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def current_date_view(request):
    time = datetime.now()
    return HttpResponse(time)


def goodbye_view(request):
    return HttpResponse("Goodbye user !")


def product_list_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        return render(request,
                      "product/product_list.html",
                      context={"products": products})

