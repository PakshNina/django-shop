from ..models.shop import Product


def get_products():
    return Product.objects.filter(quantity__gt=0)
