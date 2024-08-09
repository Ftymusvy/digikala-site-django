from django.shortcuts import render 
# باید در ابتدا لیست محصولاتمان را بگیریم 
from .models import Product

def helloworld(request):
    all_products = Product.objects.all()
    return render(request , 'index.html' , {'products' : all_products})


