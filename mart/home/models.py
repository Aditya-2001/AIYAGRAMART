from django.db import models

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
    total_numberof_products=models.IntegerField()

    def __str__(self):
        return self.name

class Orders(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product_ordered=models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_id_order=models.IntegerField(default=0)

    def __str__(self):
        return self.transaction_id_order

class UsersOrders(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    product_ordered=models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    transaction_id_user=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
