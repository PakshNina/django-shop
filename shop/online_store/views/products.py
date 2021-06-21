from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .mixins import CartInformationMixin
from ..core.utils import get_products, get_product_by_id
from ..forms.order_form import AddToCartForm


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
                self._create_entities_in_session(product, quantity)
                messages.add_message(request, messages.SUCCESS, f'Успешно добавлено "{product.name}" x {quantity} шт.')
                form = self.form_class()
                context = self.get_context_data()
                context['form'] = form
        return render(request, self.template_name, context)

    def _create_entities_in_session(self, product, quantity):
        order_entities = self.request.session.get('order_entities', {})
        product_id_key = str(product.id)
        order_entities.setdefault(product_id_key, {'name': product.name, 'price': product.price, 'quantity': 0})
        order_entities[product_id_key]['quantity'] += quantity
        self.request.session['order_entities'] = order_entities


