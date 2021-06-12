from django.urls import path
from .views.shop_page import ShopPageView


urlpatterns = [
    path('', ShopPageView.as_view(), name='shop'),
    ]
