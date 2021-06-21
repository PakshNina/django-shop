from django.urls import path
from .views.products import MainPageView, ProductPageView
from .views.create_order import CartPageView, CreateOrderView


urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
    path('product/<int:id>', ProductPageView.as_view(), name='product-page'),
    path('cart/', CartPageView.as_view(), name='user-cart'),
    path('create_order/', CreateOrderView.as_view(), name='create-order'),
]
