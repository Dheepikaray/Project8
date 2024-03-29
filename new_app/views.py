# from django.contrib import messages
# from django.contrib.auth import authenticate
# from django.shortcuts import render, redirect
#
# from new_app.forms import CustomerForm, RegistrationForm
#
#
# # Create your views here.
#
# def new(request):
#     return render(request,'base.html')
#
# def admin(request):
#     return render(request,'index.html')
#
# def login(request):
#     return render(request, 'login.html')
#
#
# def cust_register(request):
#     cust_form = CustomerForm()
#     reg_form = RegistrationForm()
#
#
#
#     if request.method == 'POST':
#         cust_form = CustomerForm(request.POST, request.FILES)
#         reg_form = RegistrationForm(request.POST)
#         if cust_form.is_valid() and reg_form.is_valid():
#             reg1 = reg_form.save(commit=False)
#             reg1.is_student = True
#             reg1.save()
#             stud1 = cust_form.save(commit=False)
#             stud1.user = reg1
#             stud1.save()
#             return redirect('login')
#         # Render the form with errors if it's not valid
#
#     return render(request, "customer.html", {"reg_form": reg_form, "cust_form": cust_form})
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username') #username is same as in the login.html page
#         print(username)
#         password = request.POST.get('pass') #pass is same in the login.html page
#         print(password)
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
#             if user.is_staff:
#                 return redirect('index') #base is the path name redirect to admin page
#             elif user.is_customer:
#                 return redirect('index') #student is the path name redirect to admin page
#
#         else:
#             messages.info(request, 'Invalid Credentials')
#     return render(request, 'login.html')

from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings


def home_view(request):
    products = models.Product.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'ecom/index1.html', {'products': products, 'product_count_in_cart': product_count_in_cart})


# for showing login button for admin(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


def customer_signup_view(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request, 'ecom/customersignup.html', context=mydict)


