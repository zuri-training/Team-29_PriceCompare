from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

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
    slug = models.SlugField(max_length=500,  null=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name+' '+str(self.id))
        super().save(*args, **kwargs)
        pass 
    
    def get_absolute_url(self):
        return reverse("Haggle:compare", kwargs={"slug": self.slug})



class ProductComment(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('productDetails', on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment {} by {} '.format(self.body, self.author)
