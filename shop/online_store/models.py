from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', help_text='Название продукта')
    description = models.TextField(verbose_name='Описание', help_text='Описание продукта')
    price = models.FloatField(verbose_name='Цена', help_text='Цена за одну штуку')
    quantity = models.IntegerField(verbose_name='Количество', help_text='Количество товара на складе')
