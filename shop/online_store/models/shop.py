from django.db import models
from django.utils import timezone

from .choices import OrderStatuses, ORDERS_STATUS_CHOICES
from .validators import phone_validator


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', help_text='Название товара')
    description = models.TextField(verbose_name='Описание', help_text='Описание товара')
    price = models.FloatField(verbose_name='Цена', help_text='Цена за одну штуку')
    quantity = models.PositiveIntegerField(verbose_name='Количество', help_text='Количество товара на складе')

    def __str__(self):
        return self.name


class Order(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    state = models.CharField(max_length=10, choices=ORDERS_STATUS_CHOICES, default=OrderStatuses.CREATED)
    customer = models.ForeignKey('Customer', related_name='customer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Заказ {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name='product', on_delete=models.CASCADE, null=True)
    product_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.order}, {self.product.name}, {self.product_quantity}'


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя покупателя')
    address = models.CharField(max_length=200, verbose_name='Адрес покупателя')
    phone = models.CharField(max_length=15, validators=[phone_validator], verbose_name='Телефон')

    def __str__(self):
        return f'{self.name}, {self.phone}'
