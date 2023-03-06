from django.urls import path
from ecomstore import settings
from . import views
urlpatterns = [
    path('', views.show_checkout, name='checkout'),
    path('receipt/', views.receipt,  name='checkout_receipt'),
]