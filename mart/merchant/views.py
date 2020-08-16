from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def login_request_merchant(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('merchant_home')
    else:
        return render(request,"merchant/login_request_merchant.html",context={})

def merchant_home(request):
    return render(request,"merchant/merchant_home.html",context={})

def mart_merchant(request):
    return redirect('home')

def logout_request_merchant(request):
    logout(request)
    return redirect('login_request_merchant')

def check_user_merchant(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('merchant_home')
            else:
                return render(request,"merchant/login_request_merchant.html",context={"user_is_not_staff": True})
        else:
            return render(request,"merchant/login_request_merchant.html",context={"error": True})
    
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")