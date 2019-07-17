from django.urls import path
from . import views

urlpatterns = [
    path('show_cart', views.show_cart,  name = 'show-cart')    
]
