from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class productDetails(models.Model):
    name = models.CharField(max_length= 50  , null= False)
    imageLink = models.CharField(max_length= 50 , null= False)
    ratings = models.CharField(max_length= 50 , null= False)
    price = models.CharField(max_length= 50 , null= False)
    merchantName = models.CharField(max_length=40 , null= False)
    brand = models.CharField(max_length=40 , null= False )
    category = models.CharField(max_length= 50 , null= False)



class ProductComment(models.Model):
    author = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('productDetails', on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment {} by {} '.format(self.body, self.author)
