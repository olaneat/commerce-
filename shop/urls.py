from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<slug>', views.category_detail, name = 'category-detail'),
    path('product-list', views.product_list, name='product-list'),
    re_path(r'^product-detal/(?P<details>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})', \
        views.product_detail, name = 'product-detail'),
    #path('product-detail/<slug>', views.product_detail , name = 'product-detail')
    ]
