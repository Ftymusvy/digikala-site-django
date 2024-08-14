from django.urls import path , include
from . import views 

urlpatterns = [
    
    path('' , views.helloworld , name="home"),
    path('about/' , views.about , name="about"),
    path('login/' , views.login_user , name="login"),
    path('logout/' , views.logout_user , name="logout"),
    path('signup/' , views.signup_user , name = "signup"),
    path('product/<int:pk>' , views.product , name = "product"),#بعد پروداکت یک متغیر عددی قرار داده شود که این مسیر فراخوانی شود
]
