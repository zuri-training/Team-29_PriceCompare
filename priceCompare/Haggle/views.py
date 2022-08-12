from django.shortcuts import render
from .models import productDetails, ProductComment
from .forms import CommentForm
from django.views.generic import ListView
import random
# Create your views here.

def faq(request):
    return render(request, 'faq.html')


def Home(request):
    product = productDetails.objects.all()
    return render(request, 'index.html', {'product':product} )


class SearchResultView(ListView):
    model = productDetails
    template_name = 'search.html'

    def search(self, mode='default', ):
        search_value = self.request.GET.get('search')
        search_value = search_value.strip()
        if mode == 'default':
            results = productDetails.objects.filter(name__icontains=search_value)
            random.Random(4).shuffle(results)
        elif mode == 'low_to_high':
            results = productDetails.objects.filter(name__icontains=search_value).order_by('price')
        elif mode == 'high_to_low':
            results = productDetails.objects.filter(name__icontains=search_value).order_by('-price')
       # elif mode == 'filter':
        #results = productDetails.objects.filter(name__icontains=search_value).filter(


        return results



def pricecompare(request, pk):
    product = productDetails.objects.get(pk=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.author
            instance.save()
    comment = ProductComment.objects.filter(product=product)
    context= {
        'product': product,
        'comment': comment,
        'form': form
    }
    return render(request, 'comparison.html', context)


