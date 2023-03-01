from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='catalog_home'),
    # (r'^$', 'index', {'template_name': 'catalog/index.html'}, 'catalog-home'),
    path('category/<slug:slug>', views.show_category, name='catalog_category'),
    # (r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',
    #  {'template_name': 'catalog/category.html'}, 'catalog_category'),
    path('product/<slug:slug>', views.show_product, name='catalog_product'),
    # (r'^product/(?P<product_slug>[-\w]+)/$', 'show_product',
    #  {'template_name': 'catalog/product.html'}, 'catalog_product'),
]
