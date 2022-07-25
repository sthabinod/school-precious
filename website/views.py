from django.shortcuts import render

from django.core.mail import send_mail
from Ingwaram_01 import settings

def index(request):
  
    return render(request, "index.html")

