# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=1000, null=True)
    description=models.CharField(max_length=10000, null=True)
    warranty_time_in_months=models.IntegerField(default=0)
    manufacturing_date=models.DateTimeField(default=datetime.now(), blank=True)
    manufacturing_company=models.CharField(max_length=1000, null=True)
    company_contact_number=models.CharField(max_length=12)
    company_email=models.EmailField(max_length=50)
    price=models.FloatField()
    stock=models.IntegerField()
    search_tags=models.CharField(max_length=1000, null=True)
    image_1=models.ImageField(null=True, blank=True, upload_to='post_images/')
    image_2=models.ImageField(null=True, blank=True, upload_to='post_images/')
    image_3=models.ImageField(null=True, blank=True, upload_to='post_images/')
    image_4=models.ImageField(null=True, blank=True, upload_to='post_images/')
    image_5=models.ImageField(null=True, blank=True, upload_to='post_images/')
    created_at=models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    product_ordered=models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_id_order=models.IntegerField(default=0)
    created_at=models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.transaction_id_order

class UsersOrders(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    product_ordered=models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    transaction_id_user=models.IntegerField(default=0)
    created_at=models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.customer.username
