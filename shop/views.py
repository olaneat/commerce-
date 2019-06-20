from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render, get_object_or_404, reverse, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    collection = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/index.html', locals())

def category_detail(request, slug):
    category_list = Category.objects.all().filter(id = 1)
    return render(request, 'shop/product-list.html', locals()) 

def product_list(request):
    product = Product.objects.all()
    paginator = Paginator(product, 25)
    page = request.GET.get('page')
    try: 
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    return render(request, 'shop/product-list.html', {'page': page})

def product_detail(request, details, year, month, day  ):
    
    details = get_object_or_404(Product, slug = details,\
                                       created__year = year,\
                                       created__month = month,\
                                       created__day = day)
    #context = {'item': item, 'details': details}
    return render( request, 'shop/product-detail.html', {'details': details})
    