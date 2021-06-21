from django.views.generic import TemplateView

from ..core.utils import get_products, get_product_by_id


class MainPageView(TemplateView):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = get_products()
        context['products'] = products
        return context


class ProductPageView(TemplateView):
    template_name = 'product_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = kwargs.get('id')
        product = get_product_by_id(product_id)
        context['product'] = product
        return context
