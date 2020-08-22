from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from home.models import Product
from home.forms import UserForm,ProductForm

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

def register_merchant(request):
    return render(request,"merchant/register_merchant.html",context={})

def find_user_merchant(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        username=request.POST.get("username")
        email=request.POST.get("email")
        try:
            checker = User.objects.get(email=email)
            return render(request,"merchant/register_merchant.html",context={"wrong_email": True})
        except:
            try:
                checker = User.objects.get(username=username)
                return render(request,"merchant/register_merchant.html",context={"wrong_username": True})
            except:
                if form.is_valid():
                    first_name = request.POST.get("first_name")
                    last_name = request.POST.get("last_name")   
                    password = request.POST.get("password2")
                    user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                    user.set_password(password)
                    user.is_staff=True
                    user.save()
                    return redirect('login_request_merchant')
                else:
                    return render(request,"merchant/register_merchant.html",context={"wrong_password": True})
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")

def create_product_merchant(request):
    if request.method =="POST":
        form=ProductForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()        
            return redirect('mart_merchant')
        else:
            return HttpResponse("<h1>This product can't be added</h1>")
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")