from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
import time

# Create your views here.

def main(request):
    return render(request,"base.html")

def send_email(request):
    email = request.POST["email"]
    subject = request.POST["subject"]
    name = request.user.username
    if subject and email:
        messages.info(request,"succes")
        return render(request, "form.html")
    else:
        messages.info(request, "nop")
        return redirect("main")
