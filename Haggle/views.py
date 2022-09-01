
from itertools import product
import queue
from unicodedata import category, name
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin

from django.db.models import Q
from django.core.paginator import Paginator




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

def profilecard(request):
    return render(request, 'profilecard.html')

def contactPage(request):
    return render(request, 'contact.html')
def Home(request):
    product = productDetails.objects.all()
    return render(request, 'index.html', {'product':product} )

def privacy(request):
    return render(request, 'privacy.html')


class SearchResultView(ListView):
    model = productDetails
    template_name = 'search.html'

    def get_queryset(self,mode='default'):
        search_value = self.request.GET.get('q')
        search_value = search_value.strip()
        if mode == 'default':
            results = list(productDetails.objects.filter(name__icontains=search_value))
            random.Random(4).shuffle(results)
        elif mode == 'low_to_high':
            results = productDetails.objects.filter(name__icontains=search_value)
        elif mode == 'high_to_low':
            results = productDetails.objects.filter(name__icontains=search_value)
        return results
    
    def get_context_data(self, **kwargs):
        product_list = self.get_queryset()
        page = self.request.GET.get('page', 1)
        paginator = Paginator(product_list, 20)
        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        context=super().get_context_data(**kwargs)
        context['products']=product
        return context


    


class PriceCompareView(FormMixin, DetailView):
    model = productDetails
    template_name = 'comparison.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('Haggle:compare', kwargs={'slug': self.object.slug})

    def get_product(self, *args, **kwargs):
        return get_object_or_404(productDetails,slug=self.kwargs['slug'])
    
    def product_comparison_fetch(self):
        import re
        product=self.get_product()
        brand= product.brand
        merchant=product.merchantName
        name=product.name
        reduced_name=re.search(f'{brand.lower()}(.+)',name.lower()).group()
        brands_list=list(productDetails.objects.values_list('brand',flat=True).distinct())

        def get_valid_query(merchant):

            case_1=' '.join(reduced_name.split()[0:4])
            case_2=' '.join(reduced_name.split()[0:3])
            case_3=' '.join(reduced_name.split()[0:2])
            case_4= brand + ' ' + reduced_name.split()[2]

            if productDetails.objects.filter(Q(merchantName=merchant) & Q(name__icontains=case_1)).exists():
                query_value=case_1
            elif productDetails.objects.filter(Q(merchantName=merchant) & Q(name__icontains=case_2)).exists():
                query_value=case_2
            elif productDetails.objects.filter(Q(merchantName=merchant) & Q (name__icontains=case_3)).exists() and (case_3.split()[0]!='apple'):
                query_value=case_3
            elif productDetails.objects.filter(Q(merchantName=merchant) & Q(name__icontains=case_4)).exists():
                query_value= case_4
            else:
                query_value=brand
            
            return query_value

        slot_query_value=get_valid_query('Slot')
        jumia_query_value=get_valid_query('Jumia')
        konga_query_value=get_valid_query('Konga')
        Slot,Jumia,Konga=1,2,3
        query_map={Slot:[slot_query_value,'Slot'],Jumia:[jumia_query_value, 'Jumia'],Konga:[konga_query_value,'Konga']}
        

        
        for i in list(query_map):
            product_merchant_name=query_map[i][1]
            query_value=query_map[i][0].split()
            if query_map[i][0] in brands_list:
                i_new=productDetails.objects.filter(Q(merchantName=product_merchant_name) & Q(name__icontains=query_map[i][0]) & Q(price__lte=product.price) & Q(category=product.category)).order_by('-price')
                query_map[i_new]=query_map.pop(i)
            else:
                i_new=productDetails.objects.filter(Q(merchantName=product_merchant_name) & Q (name__icontains=query_map[i][0])).order_by('price')
                query_map[i_new]=query_map.pop(i)

        return_list=[]
        for i in query_map:
            if i.exists() and i[0].merchantName!=merchant:
                return_list.append(i[0])
        return return_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product=self.get_product()
        context['product'] = product
        context['comparisons'] = self.product_comparison_fetch()
        context['comments'] = ProductComment.objects.filter(product=product.id).order_by('created_on')
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
        return super().form_valid(form)


class ProductListView(ListView):
    model = productDetails
    template_name = 'productlist.html'

    def get_queryset(self):
        results = list(productDetails.objects.filter(Q(category=self.kwargs.get('category')) & Q(brand__icontains=self.kwargs.get('brand')))) 
        random.Random(4).shuffle(results)
        return results

    
    
    def get_context_data(self, **kwargs):
        product_list = self.get_queryset()
        page = self.request.GET.get('page', 1)
        paginator = Paginator(product_list, 100)
        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        context=super().get_context_data(**kwargs)
        context['products']=product
        return context
