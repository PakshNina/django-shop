from django.urls import path
from .views.shop_views import MainPageView, ProductPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
    path('product/<int:id>', ProductPageView.as_view(), name='product-page')
]
