from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage,send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import time

# Create your views here.

def main(request):
    return render(request,"base.html")

def send_email(request):
    email = request.POST["email"]
    subject = request.POST["subject"]
    message = request.POST["message"]
    name = request.user.username
    if subject and email:
        send_mail(
            subject,
            message,
            'sadravalorant@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request,"your email has been sent")
        return redirect("main")
    else:
        messages.error(request, "there is something wrong with your form")
        return redirect("main")
