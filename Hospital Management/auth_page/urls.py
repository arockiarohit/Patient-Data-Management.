from django.urls import path
from .views import *

app_name = "auth_page"

urlpatterns = [
    path("loginpage/", loginpage, name="login"),
    path("logout/", Logoutpage1, name="logout"),
    path("registerpage/", registerpage, name="register"),
]
