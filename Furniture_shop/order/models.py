from django.db import models
from django.contrib.auth.models import User
from itertools import product
from product.models import Product
import uuid

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = {
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    }
    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED )
    payment_intent = models.CharField(max_length=255, blank=True, null=True)
    order_uuid = models.UUIDField(null=False, blank=False, unique=True, editable=False, default=uuid.uuid4)

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())

    def get_order_display_price(self):
        return sum(item.product.get_display_price() * item.quantity for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name = 'items', on_delete=models.CASCADE)    
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)