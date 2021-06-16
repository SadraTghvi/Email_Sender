from django.contrib.auth import logout as system_logout
from django.shortcuts import redirect, render
from django.contrib.auth.views import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.


def main(request):
    return render(request,"account_base.html")

class AccountLogin(LoginView):
    template_name = 'login.html'
    fields = "__all__"
    redirect_authenticated_user = False
    
    def get_success_url(self):
        messages.success(self.request,"You Have Logged In successfuly")
        return reverse_lazy("main:main")


def logout(e):
    system_logout(e)
    return HttpResponseRedirect('/')

class CustomLogoutView(LogoutView):
    template_name = "todo_list/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("main:main")

class AccountSignup(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("main:main")

    def form_invalid(self, form):
        messages.error("Something Was Wrong With Your Form")
        return super(AccountSignup, self).form_invalid(form)
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(AccountSignup,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("main:main")
        return super(AccountSignup,self).get(*args,**kwargs)

# TODO:
# class AccountSignin():


# class AccountSignout():
