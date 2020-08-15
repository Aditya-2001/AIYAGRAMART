from django.contrib import admin
from .models import UsersOrders,Product,Orders
# Register your models here.
admin.site.register(UsersOrders)
admin.site.register(Product)
admin.site.register(Orders)