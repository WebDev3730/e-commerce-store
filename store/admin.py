from django.contrib import admin
from .models import Product, CartItem, Cart, Order, OrderItem
# Register your models here.

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)