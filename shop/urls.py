from django.contrib import admin
from django.urls import path
from .views import showcategories,showproducts
from cart.views import add_cart,cart




urlpatterns = [

    path('shop/',showcategories,name='shop'),
    path('showproducts/<slug:category>/', showproducts),


]