from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import FormView

from .mixins import CartInformationMixin
from ..core.utils import get_total_price, create_order
from ..forms.order_form import CartForm


class CartPageView(CartInformationMixin, FormView):
    template_name = 'user_cart.html'
    form_class = CartForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context = self._update_session_with_order_info(context)
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('clear_cart', False):
            self._clean_order_entities()
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def _update_session_with_order_info(self, context):
        order_entities = self.request.session.get('order_entities', {})
        context['order_entities'] = order_entities
        context['total_price'] = get_total_price(order_entities)
        return context

    def _clean_order_entities(self):
        del self.request.session['order_entities']


class CreateOrderView(CartPageView):
    template_name = 'create_order.html'
    success_template = 'success.html'
    form_class = CartForm

    def dispatch(self, request, *args, **kwargs):
        context = super().get_context_data()
        if self._cart_is_empty(context):
            return redirect('main-page')
        return super().dispatch(request)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = self.get_context_data()
        if form.is_valid():
            cleaned_data = form.cleaned_data
            customer, comment = self._process_form_data(cleaned_data)
            order = create_order(context.get('order_entities'), customer, comment)
            self._clean_order_entities()
            context = self.get_context_data()
            context['order'] = order
            return render(request, self.success_template, context)
        messages.add_message(request, messages.ERROR, 'Произошла ошибка, попробуйте еще раз.')
        return render(request, self.template_name, context)

    def _cart_is_empty(self, context):
        return not context.get('order_entities', False)

    def _process_form_data(self, cleaned_data):
        comment = cleaned_data.get('comment')
        customer_data = {field: cleaned_data.get(field) for field in ['name', 'address', 'phone']}
        return customer_data, comment
