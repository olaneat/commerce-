from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'meta_keywords', 'price', 'available', 'description']
    list_display_links = ('name',)
    list_editable = ['price', 'description', 'available']
    search_fields = ['name', 'brand']
    prepopulated_fields = {'slug' : ('name',)}
    ordering = ['created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'slug']
    list_display_links = ['name']
    prepopulated_fields = {'slug' : ('name',)}
