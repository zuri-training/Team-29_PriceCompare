print("testinggggg")
print('iio')
from ..models import productDetails

# print(len(list(productDetails.objects.values_list('productLink', flat=True))))
print(len(productDetails.objects.values()))
print(len(productDetails.objects.filter(merchantName='Slot').filter(brand='Apple').filter(category='phone').values()))

# print(productDetails.objects.filter(merchantName='Jumia').filter(brand='Apple').filter(category='laptop').values()['price'])
# print(productDetails.objects.filter(merchantName='Jumia').values('brand').distinct().count())
# print(productDetails.objects.values()[8630])


print(productDetails.objects.order_by('-price').all()[0].name)


# print(len(list(productDetails.objects.values_list('price', flat=True))))



