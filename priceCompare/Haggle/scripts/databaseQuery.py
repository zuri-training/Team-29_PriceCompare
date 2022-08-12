import random
from ..models import productDetails
import re
model=productDetails
def search(search_value,minimum,maximum,mode='default'):
    search_value=search_value.strip()
    if mode=='default':
        results= model.objects.filter(name__icontains=search_value)
        random.Random(4).shuffle(results)
    elif mode=='low_to_high':
        results=model.objects.filter(name__icontains=search_value).order_by('price')
    elif mode=='high_to_low':
        results=model.objects.filter(name__icontains=search_value).order_by('-price')
    elif mode=='filter':
        results=model.objects.filter(name__icontains=search_value).filter(price__in=[i for i in range(minimum,maximum+1)])
    
    return results

def product_comparison_fetch(product_name):
    brand= model.objects.filter(name=product_name)[0].brand
    reduced_name=re.search(f'{brand}(.+)',product_name).group()

    #CASES FOR QUERY VALUE
    case_1=' '.join(reduced_name.split()[0:4])
    case_2=' '.join(reduced_name.split()[0:3])
    case_3=' '.join(reduced_name.split()[0:2])
    case_4= brand + ' ' + reduced_name.split()[2]

    if model.objects.filter(name__icontains=case_1).exists():
        query_value=case_1
    elif model.objects.filter(name__icontains=case_2).exists():
        query_value=case_2
    elif model.objects.filter(name__icontains=case_3).exists():
        query_value=case_3
    elif model.objects.filter(name__icontains=case_4).exists():
        query_value= case_4
    else:
        query_value=brand

    slot=model.objects.filter(merchantName='Slot').filter(name__icontains=query_value).order_by('price')
    jumia=model.objects.filter(merchantName='Jumia').filter(name__icontains=query_value).order_by('price')
    konga=model.objects.filter(merchantName='Konga').filter(name__icontains=query_value).order_by('price')
    
    result_list=[slot,jumia,konga]
    return_list=[]
        
    for i in result_list:
        if i.exists():
            return_list.append(i[0])
    
    return return_list



    
