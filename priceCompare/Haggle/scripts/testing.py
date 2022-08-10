print("testinggggg")
print('iio')
from ..models import productDetails

print(len(list(productDetails.objects.values_list('productLink', flat=True))))
print(len(productDetails.objects.filter(brand="Nokia").filter(merchantName="Konga").values()))