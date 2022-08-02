from multiprocessing import context
from webbrowser import get
from django.forms import Form
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
#AUTHENTICATION
def landing(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        return render(request, 'users/landing.html')

@login_required(login_url='login')
def home(request):
    return render(request,'users/home.html' )

def signup(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' +  user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'users/signup.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
            
        context = {}
        return render(request, 'users/login.html', context)


def logoutuser(request):
    logout(request)


    return redirect('login')