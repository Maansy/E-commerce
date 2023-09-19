from django.contrib import admin

# Register your models here.

from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added', 'user']
    list_editable = ['user']
    list_per_page = 20

admin.site.register(Cart,CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'active']
    list_editable = ['quantity', 'active']
    list_per_page = 20

admin.site.register(CartItem,CartItemAdmin)