from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

import product.models
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


def product_detail_view(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)
        context = {"product": product}
        return render(
            request=request,
            template_name="product/product_detail.html",
            context=context
        )
