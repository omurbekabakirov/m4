from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from product.forms import ProductForm, ProductForm2, ReviewForm,CategoryForm
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


def create_review_view(request,product_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if not form.is_valid():
           return render(request=request, template_name="product/product_detail.html", context={"form": form})
        review = form.save(commit=False)
        review.product_id = product_id
        review.save()
        return redirect(f"/product/{product_id}/")


def create_product_view(request):
    if request.method == "GET":
        form = ProductForm2(request.POST, request.FILES)
        return render(
            request=request,
            template_name="product/create_product.html",
            context={"form": form}
        )
    elif request.method == "POST":
        form = ProductForm2(request.POST, request.FILES)

        if not form.is_valid():
            return render(
                request=request, template_name="product/create_product.html",context={"form":form}
            )
        form.save()
        return redirect("/product/")


def create_category_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if not form.is_valid():
            return render(
                request=request, template_name="product/create_product.html",context={"form":form}
            )
        form.save()
        return redirect("/product/")