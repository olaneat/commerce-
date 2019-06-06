from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 130, unique = True)
    available = models.BooleanField(default= True)
    meta_keywords = models.CharField(max_length = 150)
    meta_description = models.CharField(max_length = 150)
    created = models.DateTimeField(auto_now= True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'catergories'
        ordering = ['created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category-detail", args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    slug = models.SlugField(max_length= 50, unique = True) 
    brand = models.CharField(max_length = 100)
    old_price = models.DecimalField(max_digits= 9, decimal_places= 2, default = 0.00)
    price = models.DecimalField(max_digits = 9, decimal_places = 2, default = 0.00)
    image = models.ImageField(upload_to = 'product_imgs', blank = True)
    best_seller = models.BooleanField(default=False)
    category = models.ManyToManyField(Category )
    description = models.TextField()
    created = models.DateTimeField(auto_now= True)

    class meta: 
        db_name = 'Product'
        ordering = [' -created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cat", args= [self.slug,
                                self.created.year,
                                self.created.strftime('%m'),
                                self.created.strftime('%d')])
    
      