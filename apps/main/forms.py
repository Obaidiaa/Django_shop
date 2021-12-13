from django import forms
from django.forms.models import ModelForm 
from .models import ProductModel
import os 
import uuid
class ProductAddForm(forms.ModelForm):
    product_name = forms.CharField(label='name', max_length=100)
    product_skd = forms.CharField(label='skd', max_length=50)
    product_price = forms.DecimalField(label='price',max_digits=5)
    product_stock = forms.DecimalField(label='stock',max_digits=5)
    product_desc = forms.CharField(label='desc',max_length=240)
    product_image = forms.ImageField(label='image',required=True) 
    class Meta:
        model = ProductModel
        fields = "__all__" 