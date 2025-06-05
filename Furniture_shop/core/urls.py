from django.urls import path, include
from .views import homepage, shop
from product.views import product

urlpatterns = [
    path('',homepage, name='homepage'),
    path('shop/', shop, name='shop'),
    path('product/', product, name='product'),
]