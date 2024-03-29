from django.contrib.auth.models import AbstractUser, User

from django.db import models
from django.db.models import BooleanField


# Create your models here.
# class Register(AbstractUser):
#     is_customer = models.BooleanField(default=True)
#
# class User_Customer(models.Model):
#     user = models.ForeignKey('Register',on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=100)
#     address = models.TextField(max_length=100)
#     cus_no = models.CharField(max_length=100)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Product(models.Model):
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name





