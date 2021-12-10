from os import name
from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addProduct/',views.addProduct,name='addProduct'),
    url(r'^load_product/$', views.load_product, name='amount'),
]