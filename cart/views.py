from .models import Cart
from django.shortcuts import reverse, render

def show_cart(request):
    cart_list = Cart.objects.count()
    return render(request, 'cart/show_cart.html', {'cart_list': cart_list})