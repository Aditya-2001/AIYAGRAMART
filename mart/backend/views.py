from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def login_request(request):
    if request.user.is_authenticated and request.user.is_staff and request.user.is_superuser:
        return redirect('backend_home')
    else:
        return render(request,"backend/login_page.html",context={})

def mart(request):
    return render(request,"home/home_page.html",context={})

def backend_home(request):
    return render(request,"backend/backend_home.html",context={})

def logout_request(request):
    logout(request)
    return redirect('login_request')

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
