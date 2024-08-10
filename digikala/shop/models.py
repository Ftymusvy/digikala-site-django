from django.db import models
import datetime
from django.core.validators import MinValueValidator , MaxValueValidator

#دسته بندی
class Category(models.Model):
    name = models.CharField(max_length= 20)

    def __str__(self):
        return self.name

#مشتری
class Customer(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    phone = models.CharField(max_length= 20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
#محصول
class Product(models.Model):
     name = models.CharField(max_length= 40)
     discription=models.CharField(max_length=500 ,default='',blank=True ,null=True)
     price = models.DecimalField(default=0 , decimal_places=0 , max_digits=12 )
     category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
     picture = models.ImageField(upload_to='upload/product/')
     star = models.IntegerField(default=0 , validators=[MaxValueValidator(5),MinValueValidator(0)])
     is_sale = models.BooleanField(default=False) # ایا این محصول در تخفیف ویژه هست یا خیر 
     sale_price = models.DecimalField(default=0 , decimal_places=0 , max_digits=12 ) #در فروش ویژه قیمتش چقدر هست ؟


     def __str__(self):
        return self.name
     
#سفارش
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE )
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=400 ,default='' , blank=True) # حتما مقدار بلنک را فالس میزاریم چون سایتی مثل دیجی کالا حتما نیاز به ادرس دارد تا از سمت مشتری وارد کنیم
    phone = models.CharField(max_length= 20 , blank=True)
    date = models.DateField(default=datetime.datetime.today())
    
    status = models.BooleanField(default=False) # وضعیت (انجام شده یا انجام نشده)


    def __str__(self):
        return self.name     