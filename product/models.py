from django.db import models


class Product(models.Model):
    name_of_product = models.CharField(max_length=100)
    image_of_product = models.ImageField(upload_to='product_image/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(default=0)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name_of_product}____{self.rating}____"



