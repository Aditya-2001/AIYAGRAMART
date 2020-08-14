from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def home(request):
    return render(request,"home/home_page.html",context={})

def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,"home/login_page.html",context={})

def signup(request):
    return render(request,"home/signup_page.html",context={})

def forgot_password(request):
    return render(request,"home/home_page.html",context={})

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