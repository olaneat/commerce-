from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<slug>', views.category_detail, name = 'category-detail'),
    path('product-list', views.product_list, name='product-list'),
    
]
