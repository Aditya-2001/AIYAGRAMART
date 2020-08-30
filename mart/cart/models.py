from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
from home.models import Product

# Create your models here.
class CartItems(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=0)