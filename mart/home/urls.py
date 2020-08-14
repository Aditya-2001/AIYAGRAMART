from django.urls import path,include
from .views import home,login_request,signup,forgot_password,match_user,terms,create_user

urlpatterns = [
    path('',home,name="home"),
    path('login_request/',login_request,name="login_request"),
    path('signup/',signup,name="signup"),
    path('forgot_password/',forgot_password,name="forgot_password"),
    path('match_user/',match_user,name="match_user"),
    path('terms/',terms,name="terms"),
    path('create_user',create_user,name="create_user")
]
