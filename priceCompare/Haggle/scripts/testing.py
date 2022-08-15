print("testinggggg")
print('iio')
from ..models import productDetails

print(len(list(productDetails.objects.values_list('productLink', flat=True))))
print(len(productDetails.objects.values()))
# print(len(productDetails.objects.filter(merchantName='Slot').filter(brand='Apple').filter(category='phone').values()))

# # # print(productDetails.objects.filter(merchantName='Jumia').filter(brand='Apple').filter(category='laptop').values()['price'])
# print(len(productDetails.objects.filter(category='phone').filter(brand='Lenovo').values()))
# # print(productDetails.objects.values()[8630])


print(productDetails.objects.order_by('-id').values('slug')[0:4])


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



