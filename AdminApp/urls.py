from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
from AdminApp.views import *

app_name = 'AdminApp'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('checkout/', checkout, name='checkout'),
    path('login/', login, name='login'),
    path('myaccount/', myaccount, name='myaccount'),
    path('register/', register, name='register'),

    path('viewoffers/', view_offers, name='viewoffers'),
    path('viewgoods/', view_goods, name='viewgoods'),
    path('updateoffer/', update_offer, name='updateoffer'),
    path('updategood/', update_good, name='updategood'),
    path('createoffer/', create_offer, name='createoffer'),
    path('creategood/', create_good, name='creategood'),
    path('deleteoffer/', delete_offer, name='deleteoffer'),
    path('deletegood/', delete_good, name='deletegood'),
]