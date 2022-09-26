import email
from email import message
from email.message import Message
from tokenize import Name
from unicodedata import name
from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import contactView

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cars(request):
    return render(request, 'cars.html')

def bikes(request):
    return render(request, 'bikes.html')

def reviews(request):
    return render(request, 'reviews.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact = contactView(name=name, email=email, message=message, date=datetime.today())
        Contact.save()
    return render(request, 'contact.html')
