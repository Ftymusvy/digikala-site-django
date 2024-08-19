from django.contrib import admin
from django.urls import path , include
# from shop.views import helloworld       به جای استفاده از این (include) را فراخوانی کردیم
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path('' , include('shop.urls')),
    path('cart/' , include('cart.urls')),
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
