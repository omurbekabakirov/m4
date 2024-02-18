from django.db import models


class Category(models.Model):
    title_of_category = models.CharField(max_length=50)

    def __str__(self):
        return self.title_of_category


class Product(models.Model):
    name_of_product = models.CharField(max_length=100)
    image_of_product = models.ImageField(upload_to='product_image/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(default=0)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        Category,
        related_name='product'
    )

    def __str__(self):
        return f"{self.name_of_product}____{self.rating}____"


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='review'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name_of_product}"
