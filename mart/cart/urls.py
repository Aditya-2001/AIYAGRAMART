from django.urls import path,include
from .views import login_request_cart,home_cart,delete_from_cart,checkout_request,confirm_order

urlpatterns = [
    path('',login_request_cart,name="login_request_cart"),
    path('home_cart/',home_cart,name="home_cart"),
    path('delete_from_cart/',delete_from_cart,name="delete_from_cart"),
    path('checkout_request/',checkout_request,name="checkout_request"),
    path('confrim_order/',confirm_order,name="confirm_order"),
]