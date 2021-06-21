from django.urls import path
from .views.shop_views import MainPageView, ProductPageView, CartPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
    path('product/<int:id>', ProductPageView.as_view(), name='product-page'),
    path('cart/', CartPageView.as_view(), name='user-cart')
]
