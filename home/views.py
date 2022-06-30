import email
from multiprocessing import context
from tokenize import Name
from unicodedata import name
from urllib import response
from django.shortcuts import render, HttpResponse
from flask import request
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "variable1" : "This is sent",
        "variable2" : "This is unsend"
    }
    return render (request , 'index.html',context)
    
def about(request):
    return render (request , 'about.html')
    
def service(request):
    return render (request , 'service.html')
   
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Successfully Submitted.')
    return render (request , 'contact.html')
    






