from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def privacy(request):
    return render(request, 'privacy.html')

def about (request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def profileCard(request):
    return render(request, 'profilecard.html')
