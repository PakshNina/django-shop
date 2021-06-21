from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from ..core.utils import get_products, get_product_by_id, get_total_price
from ..forms.order_form import AddToCartForm
from .mixins import CartInformationMixin


class MainPageView(CartInformationMixin, TemplateView):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = get_products()
        context['products'] = products
        return context


class ProductPageView(CartInformationMixin, FormView):
    template_name = 'product_page.html'
    form_class = AddToCartForm
    success_url = reverse_lazy('user-cart')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = context.get('view').kwargs.get('id')
        product = get_product_by_id(product_id)
        context['product'] = product
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = self.get_context_data()
        if form.is_valid():
            cleaned_form = form.cleaned_data
            product_id = kwargs.get('id')
            quantity = cleaned_form.get('quantity')
            if product_id:
                product = get_product_by_id(product_id)
                if quantity <= product.stock_quantity:
                    order_entities = request.session.get('order_entities', {})
                    order_entities.setdefault(
                        str(product_id),
                        {
                            'name': product.name,
                            'price': product.price,
                            'quantity': 0
                        })
                    order_entities[str(product_id)]['quantity'] += quantity
                    request.session['order_entities'] = order_entities
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        f'Успешно добавлено {quantity} цветов "{product.name}"'
                    )
                    context = self.get_context_data()
                else:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        f'К сожалению на складе осталось только {product.stock_quantity} товаров'
                    )
        return render(request, self.template_name, context)


class CartPageView(CartInformationMixin, TemplateView):
    template_name = 'user_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        order_entities = self.request.session.get('order_entities', {})
        context['order_entities'] = order_entities
        context['total_price'] = get_total_price(order_entities)
        return context
