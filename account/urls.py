from django.urls import path,include
from Account.views import *


urlpatterns = [
    path("signin/",main,name="main"),
    path("login/",AccountLogin.as_view(),name="login"),
    path("logout/",AccountLogout.as_view(),name="logout"),
]

app_name = "account"