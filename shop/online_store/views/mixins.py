from ..core.utils import get_total_items_number


class CartInformationMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_entities = self.request.session.get('order_entities', {})
        items_in_cart = get_total_items_number(order_entities)
        context.update({'items_in_cart': items_in_cart})
        return context
