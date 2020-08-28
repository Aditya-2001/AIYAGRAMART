from django.db import models

# Create your models here.
class CartItems(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=0)