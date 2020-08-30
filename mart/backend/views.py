from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from home.models import Orders
# Create your views here.

def login_request_backend(request):
    if request.user.is_authenticated and request.user.is_staff and request.user.is_superuser:
        return redirect('backend_home')
    else:
        return render(request,"backend/login_page.html",context={})

def mart(request):
    return redirect('home')

def backend_home(request):
    orders=Orders.objects.all()
    return render(request,"backend/backend_home.html",context={"orders": orders})

def logout_request_backend(request):
    logout(request)
    return redirect('login_request_backend')

def check_user(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                if user.is_superuser:
                    login(request, user)
                    return redirect('backend_home')
                else:
                    return render(request,"backend/login_page.html",context={"user_is_not_admin": True})
            else:
                return render(request,"backend/login_page.html",context={"user_is_not_staff": True})
        else:
            return render(request,"backend/login_page.html",context={"error": True})
    
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")
