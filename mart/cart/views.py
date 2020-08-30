from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .models import CartItems
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
    return HttpResponse("djfh")