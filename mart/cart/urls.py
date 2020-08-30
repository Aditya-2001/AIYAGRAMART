from django.urls import path,include
from .views import login_request_cart,home_cart,delete_from_cart

urlpatterns = [
    path('',login_request_cart,name="login_request_cart"),
    path('home_cart/',home_cart,name="home_cart"),
    path('delete_from_cart/',delete_from_cart,name="delete_from_cart"),
]