import re

from django.db import transaction
from django.db.models import QuerySet

from ..models.shop import Product, OrderItem, Order, Customer


def get_products() -> QuerySet:
    return Product.objects.filter().values('id', 'name', 'price')


def get_product_by_id(product_id: int) -> Product:
    return Product.objects.filter(id=product_id).last()


def get_total_items_number(order_entities: dict) -> int:
    return sum([item.get('quantity', 0) for item in order_entities.values()])


def get_total_price(order_entities: dict) -> int:
    return sum([item.get('price', 0) * item.get('quantity', 0) for item in order_entities.values()])


@transaction.atomic()
def create_order(order_entities: dict, customer_data: dict, comment: str) -> Order:
    customer = create_customer(customer_data)
    order = create_order_object(customer, comment)
    create_order_entities(order_entities, order)
    return order


def create_customer(customer_data: dict) -> Customer:
    phone = customer_data.get('phone')
    phone_without_code = re.sub(r'^(\+7|8)', '', phone)
    customer = Customer.objects.filter(phone__contains=phone_without_code)
    if customer.exists():
        return customer.first()
    new_customer = Customer(**customer_data)
    new_customer.save()
    return new_customer


def create_order_object(customer: Customer, comment: str) -> Order:
    order = Order(customer=customer, comment=comment)
    order.save()
    return order


def create_order_entities(order_entities: dict, order: Order) -> OrderItem:
    items = OrderItem.objects.bulk_create(
        [
            OrderItem(order=order, product=get_product_by_id(product_id), product_quantity=item['quantity'])
            for product_id, item in order_entities.items()
        ]
    )
    return items
