from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def login_request_cart(request):
    if request.user.is_authenticated :
        return redirect('home_cart')
    else :
        return redirect('login_request')

def home_cart(request):
    return render(request,"cart/home_cart.html",context={})