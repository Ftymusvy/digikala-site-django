from django.urls import path , include
from . import views 

urlpatterns = [

    path('' , views.cart_summary , name='cart_summary'),# برای دیدن سبد خرید
    path('add/' , views.cart_add , name='cart_add'),
    path('delete' , views.cart_delete , name='cart_delete'),
    path('update/' , views.cart_update , name='cart_update')
]
