from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 130, db_index= True, unique = True)
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'catergories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category-detail", args=[self.slug])

    def get_product(self):
        return Product.objects.filter(category= self.name)


class Product(models.Model):
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length= 100, db_index= True) 
    brand = models.CharField(max_length = 100)
    available = models.BooleanField(default= True)
    meta_keywords = models.CharField(max_length = 150, blank = True)
    stock = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now= True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    image = models.ImageField(upload_to = 'product_imgs', blank = True)
    best_seller = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete = 'MODEL.CASCADE', related_name='product')
    description = models.TextField()
    created = models.DateTimeField()

    class meta: 
        db_name = 'Product'
        ordering = [' -created']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", args= [self.slug,
                                self.created.year,
                                self.created.strftime('%m'),
                                self.created.strftime('%d')])
    
      