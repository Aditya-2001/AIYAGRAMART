from django.urls import path,include
from .views import home,login_request,signup,forgot_password,match_user,terms,create_user,logout_request,merchant,change_password,search_product,product_details,categorical_search

urlpatterns = [
    path('',home,name="home"),
    path('login_request/',login_request,name="login_request"),
    path('signup/',signup,name="signup"),
    path('forgot_password/',forgot_password,name="forgot_password"),
    path('change_password/',change_password,name="change_password"),
    path('match_user/',match_user,name="match_user"),
    path('terms/',terms,name="terms"),
    path('create_user/',create_user,name="create_user"),
    path('logout_request/',logout_request,name="logout_request"),
    path('merchant/',merchant,name="merchant"),
    path('search_product/',search_product,name="search_product"),
    path('product_details/',product_details,name="product_details"),
    path('categorical_search/<str:item>',categorical_search,name="categorical_search"),
]
