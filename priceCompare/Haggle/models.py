from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class productDetails(models.Model):
    name = models.CharField(max_length= 5000  , null= False)
    imageLink = models.CharField(max_length= 5000 , null= False)
    ratings = models.CharField(max_length= 50 , null= True, blank=True)
    price = models.IntegerField(null= False)
    merchantName = models.CharField(max_length=40 , null= False)
    brand = models.CharField(max_length=40 , null= False )
    category = models.CharField(max_length= 50 , null= False)
    productLink = models.CharField(max_length= 5000, null=True)



class ProductComment(models.Model):
    author = models.ForeignKey(User, null= True, blank= True, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('productDetails', on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment {} by {} '.format(self.body, self.author)
