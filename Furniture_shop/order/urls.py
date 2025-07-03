from django.urls import path
from .views import start_order, order_receipt

urlpatterns = [
    path('start_order/', start_order, name='start_order'),
    path('receipt/<int:order_id>/', order_receipt, name='order_receipt'),
]