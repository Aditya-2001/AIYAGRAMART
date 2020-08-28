from django.urls import path,include
from .views import login_request_cart,home_cart

urlpatterns = [
    path('',login_request_cart,name="login_request_cart"),
    path('home_cart/',home_cart,name="home_cart"),
]