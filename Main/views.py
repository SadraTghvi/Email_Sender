from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.

def main(request):
    return render(request,"base.html")

def send_email(request):
    stuff = request.POST
    print(stuff)
    return redirect("main")
