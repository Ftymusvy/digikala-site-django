from django.shortcuts import render, redirect
# باید در ابتدا لیست محصولاتمان را بگیریم 
from .models import Product
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages


def helloworld(request):
    all_products = Product.objects.all()
    return render(request , 'index.html' , {'products' : all_products})


def about(request):
    return render(request , 'about.html')

def login_user(request):
     if request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']

         user = authenticate(request , username= username , password=password)

     else:    
         return render(request , 'login.html')
   

def logout_user(request):
    logout(request)
    messages.success(request , ("!با موفقیت خارج شدید"))
    return redirect("home") # بعد از خارج شدن مستقیم به این صفحه هدایت شوند 