from django.shortcuts import render

# Create your views here.

def faq(request):
    return render(request, 'faq.html')


def contactPage(request):
    return render(request, 'contact.html')