from django.db.models import Q
from unicodedata import name
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
import random


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
#def landing(request):
    #if request.user.is_authenticated:
        #return redirect('home')
    #else:
        #return render(request, 'users/landing.html')

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



    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = productDetails.objects.filter(
        Q(name__icontains=query) | Q(brand__icontains=query)
        )
        return object_list
    
    #def get_context_data(self, **kwargs):
        #context=super().get_context_data(**kwargs)

        #context['product']=self.product
        #return context


    

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


class AppleCategoryView(ListView):
    model = productDetails
    template_name = 'apple.html'
    def get_queryset(self):
        object_list = productDetails.objects.filter(
        Q(category__icontains='phones') | Q(brand__icontains='apple')
        )

        return random.sample(object_list, 1123)


class SamsungCategoryView(ListView):
    model = productDetails
    template_name = 'samsung.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(brand__icontains='samsung'))

        return random.sample(object_list, 1149)


class NokiaCategoryView(ListView):
    model = productDetails
    template_name = 'nokia.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(brand__icontains='nokia'))

        return random.sample(object_list, 104)


class TechnoCategoryView(ListView):
    model = productDetails
    template_name = 'techno.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(name__icontains='techno'))

        return object_list




class InfinixCategoryView(ListView):
    model = productDetails
    template_name = 'infinix.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(brand__icontains='infinix'))

        return random.sample(object_list, 541)




class OppoCategoryView(ListView):
    model = productDetails
    template_name = 'oppo.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(brand__icontains='oppo'))

        return random.sample(object_list, 198)



class XiaomiCategoryView(ListView):
    model = productDetails
    template_name = 'xiaomi.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(brand__icontains='xiaomi'))

        return object_list


class LenovoCategoryView(ListView):
    model = productDetails
    template_name = 'apple.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(brand__icontains='lenovo'))

        return random.sample(object_list, 960)

class AsusCategoryView(ListView):
    model = productDetails
    template_name = 'asus.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(brand__icontains='asus'))

        return random.sample(object_list, 444)

class LenovoPCCategoryView(ListView):
    model = productDetails
    template_name = 'lenovopc.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(name__icontains='lenovo'))

        return random.sample(object_list, 960)


class DellCategoryView(ListView):
    model = productDetails
    template_name = 'dell.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(brand__icontains='dell'))

        return random.sample(object_list, 703)


class HpCategoryView(ListView):
    model = productDetails
    template_name = 'hp.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(brand__icontains='hp'))

        return random.sample(object_list, 1206)


class ApplePCCategoryView(ListView):
    model = productDetails
    template_name = 'applepc.html'
    def get_queryset(self):
        object_list = list(productDetails.objects.filter(
        Q(name__icontains='macbook')
        ))

        return random.sample(object_list, 157)
