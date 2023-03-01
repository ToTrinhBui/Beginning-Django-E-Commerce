from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from catalog.models import Category, Product
from django.template import RequestContext

def index(request):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render(request,"catalog/index.html",{'page_title':page_title})
    # (template_name, locals(), 
    # context_instance=RequestContext(request))

def show_category(request, slug):
    c = get_object_or_404(Category, slug=slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(request,"catalog/category.html",{'c': c, 'products': products,
    'page_title': page_title})

def show_product(request, slug):
    p = get_object_or_404(Product, slug=slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render(request,"catalog/product.html",{'p': p, 'categories':categories,
    'page_title': page_title})

