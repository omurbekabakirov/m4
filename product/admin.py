from django.contrib import admin
from product.models import (
    Product,
    Category,
    Review
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id",'name_of_product',"rating","price","created_at")
    list_editable = ("name_of_product","rating","price")


admin.site.register(Category)
admin.site.register(Review)
