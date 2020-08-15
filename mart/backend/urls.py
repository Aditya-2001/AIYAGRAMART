from django.urls import path,include
from .views import login_request,mart,backend_home,logout_request,check_user

urlpatterns = [
    path('',login_request,name="login_request"),
    path('mart/',mart,name="mart"),
    path('backend_home/',backend_home,name="backend_home"),
    path('logout_request/',logout_request,name="logout_request"),
    path('check_user/',check_user,name="check_user"),
]
