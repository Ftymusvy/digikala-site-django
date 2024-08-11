from django.urls import path , include
from .views import helloworld, about

urlpatterns = [
    
    path('' , helloworld , name="home"),
    path('about/' , about , name="about")
]
