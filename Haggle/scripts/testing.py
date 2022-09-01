print("testinggggg")
print('iio')
from ..models import productDetails
from django.db.models import Q

# print(len(list(productDetails.objects.values_list('productLink', flat=True))))

# print(len(productDetails.objects.values()))
# 

# def get_variable_name(variable):
#     return [a for a,b in locals().items() if b==variable][0]






# print(len(productDetails.objects.filter(merchantName='Slot').filter(brand='Apple').filter(category='phone').values()))

# print(productDetails.objects.filter(merchantName='Jumia').filter(brand='Apple').filter(name__icontains='iphone 13').order_by('-price').values())
# print(len(productDetails.objects.filter(category='phone').filter(brand='Lenovo').values()))
# # print(productDetails.objects.values()[8630])


# print(productDetails.objects.filter(slug='tecno-pop-5-61-2gb-ram32gb-rom-5000mah-android-10-ice-blue-2946')[0].delete())
# print(productDetails.objects.filter(merchantName='Slot').update(merchantLogo=slot_logo))
# print(productDetails.objects.filter(price__lte=207800).filter(Q(brand="Apple") | Q(brand="Samsung")).values_list('price',flat=True).order_by('-price'))
# print(list(productDetails.objects.values_list('brand',flat=True).distinct()))

# print(len(list(productDetails.objects.values_list('price', flat=True))))

# from django.template.defaultfilters import slugify
# # b='webt'
# # c=233
# # print(slugify(b+" " +str(c)))

# for i in range(6992,len(productDetails.objects.order_by('id').values())):
#     id=productDetails.objects.order_by('id').values()[i]['id']
#     name=productDetails.objects.order_by('id').values()[i]['name']
#     productDetails.objects.filter(id=id).update(slug=slugify(name+' '+str(id)))
#     print(str(i)+'A')
