from ..models.shop import Product


def get_products():
    return Product.objects.filter().values('id', 'name', 'stock_quantity', 'price').order_by('-stock_quantity')


def get_product_by_id(product_id):
    return Product.objects.filter(id=product_id).last()
