from django.urls import path,include
from .views import login_request_backend,mart,backend_home,logout_request_backend,check_user

urlpatterns = [
    path('',login_request_backend,name="login_request_backend"),
    path('mart/',mart,name="mart"),
    path('backend_home/',backend_home,name="backend_home"),
    path('logout_request_backend/',logout_request_backend,name="logout_request_backend"),
    path('check_user/',check_user,name="check_user"),
]
