from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .models import CartItems
from home.models import Orders,UsersOrders,Product
from datetime import date

# Create your views here.

def login_request_cart(request):
    if request.user.is_authenticated :
        return redirect('home_cart')
    else :
        return redirect('login_request')

def home_cart(request):
    products=CartItems.objects.filter(customer=request.user).order_by("-added_at")
    return render(request,"cart/home_cart.html",context={"products": products})

def delete_from_cart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            ID=request.POST.get("ID")
            model_delete=CartItems.objects.get(id=ID)
            model_delete.delete()
            return redirect('home_cart')
        else:
            return redirect('login_request')
    else:
        return redirect('home')

def checkout_request(request):
    if request.method =="POST":
        if request.user.is_authenticated:
            products=CartItems.objects.filter(customer=request.user).order_by("-added_at")
            
            items={}
            total_bill=0
            for product in products:
                if product.product.stock > 0:
                    flag=1
                    for key in items:
                        if key==product.product.name:
                            if items[key] < product.product.stock:
                                items[key]=items[key] + 1
                                total_bill=total_bill+product.product.price
                            flag=0
                            break  
                    if flag==1:
                        items.update({product.product.name:1})
                        total_bill=total_bill+product.product.price
                else:
                    product.delete()
            return render(request,"cart/checkout-page.html",context={"product": items, "total_bill": total_bill})
        else:
            return redirect('login_request')
    else:
        return HttpResponse("ERROR: Illegal method to order a product")

def confirm_order(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            transaction_id=123
            products=CartItems.objects.filter(customer=request.user).order_by("-added_at")
            items={}
            total_bill=0
            for product in products:
                if product.product.stock > 0:
                    flag=1
                    for key in items:
                        if key==product.product.name:
                            if items[key] < product.product.stock:
                                items[key]=items[key] + 1
                                total_bill=total_bill+product.product.price
                            flag=0
                            break  
                    if flag==1:
                        items.update({product.product.name:1})
                        total_bill=total_bill+product.product.price
                else:
                    product.delete()

            for product in products:
                for key in items:
                    if key==product.product.name:
                        if  items[key]>0:
                            items[key] = items[key] - 1
                            Orders.objects.create(customer=request.user, product_ordered=product.product)
                            UsersOrders.objects.create(customer=request.user, product_ordered=product.product)
                            ID=product.product.id
                            stock_ID=product.product.stock
                            new=Product.objects.get(id=ID)
                            new.stock = stock_ID - 1
                            new.save()
                            product.delete()
                        else:
                            product.delete()
                        break
            return HttpResponse("Order has been placed successfully")
        else:
            return redirect('login_request')
    else:
        return HttpResponse("ERROR: Illegal method to order a product")