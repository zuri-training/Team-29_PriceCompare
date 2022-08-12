import re
from ..models import productDetails

for i in range(len(productDetails.objects.order_by('id').values())):
    id=productDetails.objects.order_by('id').values()[i]['id']
    value=productDetails.objects.order_by('id') .values()[i]['price']
    productDetails.objects.filter(id=id).update(price=''.join(re.findall(r'\d+',value)))
  


 