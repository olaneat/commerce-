from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render, reverse, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    collection = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/index.html', locals())

def category_detail(request, slug):
    category_list = get_list_or_404(Category)
    return render(request, 'shop/product-list.html', locals()) 

def product_list(request):
    product = Product.object.all()
    paginator = Paginator(product, 25)
    page = request.GET.get('page')
    try: 
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    
    context = {'page':page, 'item':item}

    return render(request, 'shop/product-list.html', {'context': context})