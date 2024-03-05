from .models import Product


def create_100_posts():
    products = []
    for i in range(100):
        product = Product(
            title=f'Title {i}',
            content=f'Content {i}',
            rate=i
        )
        products.append(product)

    Product.objects.bulk_create(product)
