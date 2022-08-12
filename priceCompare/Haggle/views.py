
from unicodedata import name
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin


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

from .models import productDetails, ProductComment
from .forms import CommentForm
from django.urls import reverse
from django.views.generic import ListView
import random

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


def faq(request):
    return render(request, 'faq.html')


def contactPage(request):
    return render(request, 'contact.html')
def Home(request):
    product = productDetails.objects.all()
    return render(request, 'index.html', {'product':product} )


class SearchResultView(ListView):
    model = productDetails
    template_name = 'search.html'

    def get_queryset(self,mode='default'):
        search_value = self.request.GET.get('search')
        search_value = search_value.strip()
        self.product=get_object_or_404(productDetails,name=self.kwargs['id'])
        if mode == 'default':
            results = productDetails.objects.filter(id=self.product).filter(name__icontains=search_value)
            random.Random(4).shuffle(results)
        elif mode == 'low_to_high':
            results = productDetails.objects.filter(id=self.product).filter(name__icontains=search_value)
        elif mode == 'high_to_low':
            results = productDetails.objects.filter(id=self.product).filter(name__icontains=search_value)
        
        return results
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['product']=self.product
        return context


    

# Create your views here.

# class ProductListView(ListView):
#     model = productDetails
#     paginate_by= 50

#     results= model.objects.filter(brand=brand).filter(category=category)

#     # def get_context_data(self, **kwargs):
#     #     context=
#     #     return context

class PriceCompareView(FormMixin, DetailView):
    model = productDetails
    template_name = 'comparison.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('Haggle:product', kwargs={'pk': self.object.pk})

    def product_comparison_fetch(self):
        import re
        brand= self.object.brand
        reduced_name=re.search(f'{brand}(.+)',self.object.name).group()

        #CASES FOR QUERY VALUE
        case_1=' '.join(reduced_name.split()[0:4])
        case_2=' '.join(reduced_name.split()[0:3])
        case_3=' '.join(reduced_name.split()[0:2])
        case_4= brand + ' ' + reduced_name.split()[2]

        if productDetails.objects.filter(name__icontains=case_1).exists():
            query_value=case_1
        elif productDetails.objects.filter(name__icontains=case_2).exists():
            query_value=case_2
        elif productDetails.objects.filter(name__icontains=case_3).exists():
            query_value=case_3
        elif productDetails.objects.filter(name__icontains=case_4).exists():
            query_value= case_4
        else:
            query_value=brand

        slot=productDetails.objects.filter(merchantName='Slot').filter(name__icontains=query_value).order_by('price')
        jumia=productDetails.objects.filter(merchantName='Jumia').filter(name__icontains=query_value).order_by('price')
        konga=productDetails.objects.filter(merchantName='Konga').filter(name__icontains=query_value).order_by('price')
        
        result_list=[slot,jumia,konga]
        return_list=[]
            
        for i in result_list:
            if i.exists():
                return_list.append(i[0])
        
        return return_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object
        context['comparisons'] = self.product_comparison_fetch()
        context['comments'] = ProductComment.objects.filter(product=self.object.id).order_by('created_on')
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save(commit=False)
        return super(PriceCompareView, self).form_valid(form)


