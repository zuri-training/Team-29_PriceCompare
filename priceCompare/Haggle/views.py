from django.shortcuts import render

# Create your views here.

def faq(request):
    return render(request, 'faq.html')
def profilecard(request):
    return render(request, 'profilecard.html')
