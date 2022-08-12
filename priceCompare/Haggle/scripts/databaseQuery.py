import random
from ..models import productDetails
def search(search_value,minimum,maximum,mode='default', ):
    search_value=search_value.strip()
    if mode=='default':
        results= productDetails.objects.filter(name__icontains=search_value)
        random.Random(4).shuffle(results)
    elif mode=='low_to_high':
        results=productDetails.objects.filter(name__icontains=search_value).order_by('price')
    elif mode=='high_to_low':
        results=productDetails.objects.filter(name__icontains=search_value).order_by('-price')
    elif mode=='filter':
        results=productDetails.objects.filter(name__icontains=search_value).filter(price__in=[i for i in range(minimum,maximum+1)])
    
    return results

def product_comparison_fetch():

    #STILL IN PROGRESS

    pass

    
