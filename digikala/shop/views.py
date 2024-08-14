from django.shortcuts import render, redirect
# باید در ابتدا لیست محصولاتمان را بگیریم 
from .models import Product
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#فرمی که ساختیم ایمپورت میکنیم

from .forms import SignUpForm


def helloworld(request):
    all_products = Product.objects.all()
    return render(request , 'index.html' , {'products' : all_products})


def about(request):
    return render(request , 'about.html')

def login_user(request):
     if request.method == "POST":   # اگر از طریق نوبار کد url جیزی ارسال نشده بود ،کارهای لاگین را انجام دهد
         username = request.POST['username'] # همان اسمی که در فرم لاگاین استفاده کردیم
         password = request.POST['password']

         user = authenticate(request , username= username , password=password) #اهراز هویت کن ببین چنین یوزری وجود دارد یا خیر
         if user is not None:
             login(request , user)
             messages.success(request , ("با موفقیت وارد شدید"))
             return redirect("home")
         else:
             messages.success(request , ("مشکلی در لاگین وجود داشت"))
             return redirect("login") 

     else:    
         return render(request , 'login.html')
   

def logout_user(request):
    logout(request)
    messages.success(request , ("!با موفقیت خارج شدید"))
    return redirect("home") # بعد از خارج شدن مستقیم به این صفحه هدایت شوند


def signup_user(request):
    
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password1)
            login(request, user)

            messages.success(request, 'اکانت شما ساخته شد!')
            return redirect("home")

        else:
            messages.success(request, 'مشکلی در ثبت نام شما وجود دارد!')
            return redirect("signup")

    else:
        return render(request, 'signup.html', {'form': form})



def product(request, pk): #pk: product key
    product = Product.objects.get(id=pk)  #ینی محصولی را پیداکن که ای دی اون برابر  pk محصولی است که کاربر وارد کرده
    return render(request , 'product.html' , {'product' : product})