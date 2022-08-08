print("testinggggg")
print('iio')
from ..models import productDetails

print(len(list(productDetails.objects.values_list('productLink', flat=True))))