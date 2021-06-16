from django.urls import path, include
from Account.views import *


urlpatterns = [
    path("login/",  AccountLogin.as_view(), name="login"),
    path("logout/", logout, name="logout"),
    path("signup/", AccountSignup.as_view(), name="signup"),
]

app_name = "account"