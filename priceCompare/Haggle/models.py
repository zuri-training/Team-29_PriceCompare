from django.db import models

# Create your models here.
class productDetails(models.Model):
    name = models.CharField(max_length= 50  , null= False)
    imageLink = models.CharField(max_length= 50 , null= False)
    ratings = models.CharField(max_length= 50 , null= False)
    price = models.CharField(max_length= 50 , null= False)
    merchantName = models.CharField(max_length=40 , null= False)
    brand = models.CharField(max_length=40 , null= False )
    category = models.CharField(max_length= 50 , null= False)