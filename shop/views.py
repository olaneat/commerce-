from django.shortcuts import render
from .models import Product, Category
from cart.models import Cart            
from django.shortcuts import render, get_object_or_404, reverse, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import ProductAdminForm
from django.http import HttpResponseRedirect



def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    product = category.product_set.all()
    context = {'category':category, 'product':product }
    return render(request, 'shop/product-list.html', context)  

def product_list(request, category_slug = None):
    cat = None
    category = Category.objects.all()
    product = Product.objects.filter(available = True)
    if category_slug:
        cat = get_list_or_404(Category, slug = category_slug)
        product = product.filter(cat = cat)
    return render(request, 'shop/index.html', {
        'cat':cat,
        'category': category,
        'product': product})

def product_detail(request, details, year, month, day  ):
    details = get_object_or_404(Product, slug = details,\
                                       created__year = year,\
                                       created__month = month,\
                                       created__day = day)
    #context = {'item': item, 'details': details}
    return render( request, 'shop/product-detail.html', {'details': details})

def category_view(request):
    my_title = "Product List"
    qs = Product.objects.filter(category = request.querystring)
    category_list = ProductFilter(request.GET, queryset = qs)
    context = {'object_list': category_list, 'title': my_title}
    return render( request, context, 'product_list.html' )

def show_product(request, product_slug):
    p = get_list_or_404(Product, slug = product_slug)
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = ProductAdminForm(request, postdata)
        if form.is_valid():
            Cart.add_to_cart(request)
            if request.session_test_cookied_worked():
                request.session.delete_test_cookie()
