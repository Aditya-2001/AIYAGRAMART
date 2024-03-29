from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .forms import UserForm,ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .models import Product, Orders, UsersOrders, Query
from cart.models import CartItems
# Create your views here.
def home(request):
    product_details=Product.objects.all().order_by("-created_at")
    return render(request,"home/home_page.html",context={"products": product_details})

def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,"home/login_page.html",context={})

def signup(request):
    return render(request,"home/signup_page.html",context={})

def forgot_password(request):
    return render(request,"home/create_new_password.html",context={})

def change_password(request):
    if request.method == "POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        try:
            checker_username = User.objects.get(email=email).username
            try:
                checker1 = User.objects.get(username=username)
                checker2 = User.objects.get(username=checker_username)
                if checker1 == checker2 :
                    if password1 == password2:
                        user = User.objects.get(username=username)
                        user.set_password(password2)
                        user.save()
                        return redirect('login_request')
                    else:
                        return render(request,"home/create_new_password.html",context={"wrong_password": True})
                else:
                    return render(request,"home/create_new_password.html",context={"wrong_user_email": True})
            except:
                ender(request,"home/create_new_password.html",context={"wrong_username": True})
        except:
            return render(request,"home/create_new_password.html",context={"wrong_email": True})
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")

def match_user(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,"home/login_page.html",context={"error": True})
    
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")

def terms(request):
    return HttpResponse("<h1>Terms and Conditions: Yet to be declared</h1>")

def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        username=request.POST.get("username")
        email=request.POST.get("email")
        try:
            checker = User.objects.get(email=email)
            return render(request,"home/signup_page.html",context={"wrong_email": True})
        except:
            try:
                checker = User.objects.get(username=username)
                return render(request,"home/signup_page.html",context={"wrong_username": True})
            except:
                if form.is_valid():
                    first_name = request.POST.get("first_name")
                    last_name = request.POST.get("last_name")   
                    password = request.POST.get("password2")
                    user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                    user.set_password(password)
                    user.save()
                    return redirect('login_request')
                else:
                    return render(request,"home/signup_page.html",context={"wrong_password": True, "error": form.errors})
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")

def logout_request(request):
    logout(request)
    return redirect('home')

def merchant(request):
    return render(request,"merchant/login_request_merchant.html",context={})

def search_product(request):
    if request.method == "GET":
        search_product=request.GET.get("search_product")
        print(search_product)
        products = Product.objects.filter(search_tags__icontains=search_product).order_by("-created_at")
        all_products = Product.objects.all()
        return render(request,"home/search_material.html",context={"products": products, "all_products": all_products})
    else:
        return redirect('home')

def product_details(request):
    if request.method == "GET":
        ID=request.GET.get("ID")
        product_details=Product.objects.get(id=ID)
        all_products = Product.objects.all()
        return render(request,"home/product_details.html",context={"product": product_details, "all_products": all_products})
    else:
        return redirect('home')

def categorical_search(request,item):
    products = Product.objects.filter(search_tags__icontains=item).order_by("-created_at")
    all_products = Product.objects.all()
    return render(request,"home/search_material.html",context={"products": products, "all_products": all_products})

def query(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        Query.objects.create(name=name, email=email, message=message)
        return redirect('home')
    else:
        return redirect('home')

def about(request,item):
    if item=="company":
        return render(request,"home/about.html",context={"company": True})
    elif item=="team":
        return render(request,"home/about.html",context={"team": True})
    elif item=="career":
        return render(request,"home/about.html",context={"career": True})
    else:
        return redirect('home')

def carttemp(request):
    return redirect('login_request_cart')

def add_to_cart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            ID=request.POST.get("ID")
            product_details=Product.objects.get(id=ID)
            stock_of_product=Product.objects.get(id=ID).stock
            if stock_of_product > 0:
                user = request.user
                CartItems.objects.create(customer=request.user, product=product_details)
                return redirect('home')
            else:
                return redirect('home')
        else:
            return redirect('login_request')
    else:
        return redirect('home')

def my_order(request):
    if request.user.is_authenticated:
        orders=UsersOrders.objects.filter(customer=request.user).order_by("-created_at")
        return render(request,"home/my_orders.html",context={"orders": orders})
    else:
        return redirect('login_request')
