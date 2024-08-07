from django.contrib import admin
from django.urls import path , include
# from shop.views import helloworld       به جای استفاده از این (include) را فراخوانی کردیم

urlpatterns = [
    path("admin/", admin.site.urls),
    path('' , include('shop.urls')),
]
