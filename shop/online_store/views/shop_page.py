from django.shortcuts import render
from django.views.generic import TemplateView
from ..core.orders import get_products


class ShopPageView(TemplateView):
    template_name = 'shop.html'

    def get(self, request, *args, **kwargs):
        products = get_products()
        return render(request, self.template_name, {'products': products})
