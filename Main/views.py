from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.

def main(request):
    return render(request,"base.html")