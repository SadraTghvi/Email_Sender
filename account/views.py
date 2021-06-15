from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

# class AccountLogin(LoginView):


# class AccountLogout(LogoutView):

def main(request):
    return render(request,"account_base.html")

class AccountLogin(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = False
    def get_success_url(self):
        messages.success(self.request,"You Have Logged in successfuly")
        return reverse_lazy("main:main")
