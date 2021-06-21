from ..models.shop import Product


def get_products():
    return Product.objects.filter().values('id', 'name', 'stock_quantity', 'price').order_by('-stock_quantity')


def get_product_by_id(product_id):
    return Product.objects.filter(id=product_id).last()


def get_total_items_number(order_entities):
    return sum([item.get('quantity', 0) for item in order_entities.values()])


def get_total_price(order_entities):
    return sum([item.get('price', 0) * item.get('quantity', 0) for item in order_entities.values()])
