
import json
from os import error, stat
from django.http import request,QueryDict
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import ProductModel
from .forms import ProductAddForm

# Create your views here.
def home(request):
    return render(request,'main/home.html',context=None)

# Add product page
def addProduct(request):
        # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # d = QueryDict(request.POST)
        # print(d)
        print(request.POST)
        # print(request.POST['data'].split('&'))
        
        form = ProductAddForm(request.POST)
        # form.product_name = d.get('product_name')
        # form.product_skd = d.get('product_skd')
        # form.product_price = float(d.get('product_price'))
        # form.product_stock = float(d.get('product_stock'))
        # form.product_desc = d.get('product_desc')
        # e = ProductAddForm(form)
        # print(e)
        # print(form.errors)
        # errorForm = form.errors
        print(form.errors)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            return JsonResponse({"instance": list(ProductModel.objects.all().values())}, status=200)
        else:
            return JsonResponse({"error": list(form.errors.values())}, status=200)
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductAddForm()
        
        
        # all_entries = ProductModel.objects.count()
        return render(request,'products/add_products.html',{'form': form,'current':'all_entries'})

# load data and send it to user
def load_product(request):
    if request.method == 'GET':
        total_per_page = 10
        response_data ={'data':'123456'}
        response_data['total'] = total_per_page
    return render(request,'products/products_grid.html',response_data)