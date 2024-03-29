# from django.contrib.auth.forms import UserCreationForm
#
# from new_app.models import Register, User_Customer
# from django import forms
#
#
# class CustomUserForm(UserCreationForm):
#     class Meta:
#         model = Register
#         fields = ('username','email','first_name','last_name',)
#
#
# class RegistrationForm(UserCreationForm):
#     Username = forms.CharField()
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Register
#         fields = ('username','password1','password2')
#
# class CustomerForm(forms.ModelForm):
#     CH = (('M', 'Male'), ('F', 'Female'),('O','Other'))
#     gender = forms.CharField(widget=forms.RadioSelect(choices=CH))
#     class Meta:
#         model = User_Customer
#         fields = ('name','gender','address','cus_no',)
from django import forms
from django.contrib.auth.models import User


from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['address', 'mobile', 'profile_pic']


class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)
