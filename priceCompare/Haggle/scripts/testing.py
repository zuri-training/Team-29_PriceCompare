print("testinggggg")
print('iio')
from ..models import productDetails

# print(len(list(productDetails.objects.values_list('productLink', flat=True))))
print(len(productDetails.objects.values()))
print(len(productDetails.objects.filter(merchantName='Slot').filter(brand='Apple').filter(category='phone').values()))

# print(productDetails.objects.filter(merchantName='Jumia').filter(brand='Apple').filter(category='laptop').values()['price'])
# print(productDetails.objects.filter(merchantName='Jumia').values('brand').distinct().count())
# print(productDetails.objects.values()[8630])


print(productDetails.objects.order_by('-price').values()[0])

print(productDetails.objects.filter(price__in=[i for i in range(1000000,1050000)]).values())

# print(len(list(productDetails.objects.values_list('price', flat=True))))


