from django.shortcuts import render
from . import forms
# Create your views here.



def form_name_view(request):
    form = forms.FormName()
    return render(request, 'signup.html', {'form':form})


def login(request):
    form = forms.FormName()
    return render(request, 'signin.html', {'form':form})


def test(request):
    form = forms.FormName()
    return render(request, 'test.html', {'form':form})




