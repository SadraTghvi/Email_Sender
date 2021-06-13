from django.urls import path, include
from .views import *

urlpatterns = [
    path("",main,name="main"),
    path("send_email/", send_email, name="send_email"),
]

