from django.contrib import admin

from .permissions import CreationRestrictMixin, DeleteRestrictionMixin
from ..models.shop import Product, Order, OrderItem, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity')


@admin.register(Order)
class OrderAdmin(CreationRestrictMixin, DeleteRestrictionMixin, admin.ModelAdmin):
    list_display = ('id', 'create_at_formatted', 'state', 'customer_name', 'customer_phone')
    readonly_fields = (
        'id',
        'create_at_formatted',
        'customer_name',
        'customer_phone',
        'customer_address'
    )
    fields = (
        'id',
        'state',
        'create_at_formatted',
        'customer_name',
        'customer_phone',
        'customer_address'
    )

    def create_at_formatted(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')

    def customer_name(self, obj):
        return obj.customer.name

    def customer_phone(self, obj):
        return obj.customer.phone

    def customer_address(self, obj):
        return obj.customer.address

    create_at_formatted.short_description = 'Дата создания'
    customer_name.short_description = 'Имя покупателя'
    customer_phone.short_description = 'Телефон'


@admin.register(OrderItem)
class OrderItemAdmin(CreationRestrictMixin, DeleteRestrictionMixin, admin.ModelAdmin):
    list_display = ('order', 'product', 'product_quantity')
    readonly_fields = ('order', 'product', 'product_quantity')


@admin.register(Customer)
class CustomerAdmin(CreationRestrictMixin, admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')
    readonly_fields = (
        'name',
        'phone',
        'address',
    )
