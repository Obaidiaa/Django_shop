
import json
from os import error, stat
from django.db.models.fields.files import ImageField
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
        print(request.POST,request.FILES)
        # print(request.POST['data'].split('&'))
        
        form = ProductAddForm( data=request.POST,files=request.FILES)
        print(form.errors)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required 
            product_name = form.cleaned_data.get('product_name')
            product_skd = form.cleaned_data.get('product_skd')
            product_price = float(form.cleaned_data.get('product_price'))
            product_stock = float(form.cleaned_data.get('product_stock'))
            product_desc = form.cleaned_data.get('product_desc')
            product_image = form.cleaned_data.get('product_image')
            obj = ProductModel.objects.create( 
                                 product_name = product_name,  
                                 product_skd = product_skd,
                                 product_price = product_price,
                                 product_stock = product_stock,
                                 product_desc = product_desc,
                                 product_image = product_image 
                                 ) 
            obj.save() 
            print(obj)
            # form.save()
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