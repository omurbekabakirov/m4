from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from product.forms import ProductForm, ProductForm2, ReviewForm, CategoryForm
from product.models import Product, Category, Review
from django.db.models import Q


def hello_view(request):
    return HttpResponse("Hello ! it's my project")


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def current_date_view(request):
    time = datetime.now()
    return HttpResponse(time)


def goodbye_view(request):
    return HttpResponse("Goodbye users !")


def product_list_view(request):
    if request.method == "GET":
        search = request.GET.get('search')
        category_id = request.GET.get('category_id')
        sort = request.GET.get('sort')
        categories = Category.objects.all()
        query_params = {}
        products = Product.objects.exclude(user=request.user).all()
        if search:
            products = products.filter(
                Q(name_of_product__icontains=search) |
                Q(description__icontains=search)

            )
        if category_id:
            products = products.filter(tags=category_id)
        if sort == 'rating':
            order = request.GET.get('order')
            if order == 'asc':
                products = products.order_by('rating')
            else:
                products = products.order_by('-rating')
        elif sort == 'created_at':
            order = request.GET.get('order')
            if order == 'asc':
                products = products.order_by('created_at')
            else:
                products = products.order_by('-created_at')

        limit = 20
        max_pages = products.count() / limit
        if max_pages % 1 != 0:
            max_pages = int(max_pages) + 1
        pages = [i for i in range(1, max_pages + 1)]
        start = (int(page) - 1) * limit
        end = start + limit

        products = products[start:end]
        context = {'products': products, 'categories': categories, "pages": pages}
        return render(request,
                      "product/product_list.html",
                      context=context)


def product_detail_view(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)
        context = {"product": product}
        return render(
            request=request,
            template_name="product/product_detail.html",
            context=context
        )


def create_product_view(request):
    if request.method == 'GET':
        context = {
            "form": ProductForm2()
        }
        return render(request, 'product/create_product.html', context)
    elif request.method == 'POST':
        form = ProductForm2(request.POST, request.FILES)
        if not form.is_valid():
            context = {
                "form": form
            }
            return render(request, 'product/create_product.html', context)
        form.save()
        return redirect("/products/")


def create_category_view(request):
    if request.method == 'GET':
        context = {
            "form": CategoryForm(),
        }
        return render(request, 'product/create_category.html', context=context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if not form.is_valid():
            context = {
                "form": form
            }
            return render(request, 'product/create_category.html', context=context)
    return redirect('/products/')
