from .models import Cart
from shop.models import Product, Category
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import decimal
from django.config import settings
import random


CART_ID_SESSION_KEY = 'cart_id'

class Cart(object):
    def __init__:
        self.session = request.session
        cart = self.session.get(settings.CART_SEESION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add_cart(self, product, quantity, item_update):
        product_id = str(product.id)
        if product_id not in self.cart:
        self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if item_update:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified  = True

    def remove(self):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __len(self):
        return sum(item['product'] for item in self.cart.values())
    
    def __iter__(self):
        product_ids = self.cart.keys()
        
