from django.db import models
from shop.models import Product

class Cart (models.Model):
    cart_id =  models.CharField(max_length = 40)
    date_added = models.DateField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete = 'MODEL.CASCADE')

    class Meta: 
        ordering = ('-date_added',)
    
    def total(self):
        return self.quantity * self.product.price;

    def price(self):
        return  self.product.price;

    def name(self):      
        return self.product.name
    
    def get_absolute_url(self):
        return self.product.get_absolte_url()   
    
    def argument_quantity(self):
        self.quantity = self.quantity + int(quantity)
        self.save()
