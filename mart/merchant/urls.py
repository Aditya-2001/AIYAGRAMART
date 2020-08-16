from django.urls import path,include
from .views import login_request_merchant,merchant_home,mart_merchant,check_user_merchant,logout_request_merchant
urlpatterns = [
    path('',login_request_merchant,name="login_request_merchant"),
    path('merchant_home/',merchant_home,name="merchant_home"),
    path('mart_merchant/',mart_merchant,name="mart_merchant"),
    path('check_user_merchant/',check_user_merchant,name="check_user_merchant"),
    path('logout_request_merchant/',logout_request_merchant,name="logout_request_merchant"),
]
