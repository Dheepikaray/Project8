from django.contrib import admin

# Register your models here.
from django.contrib import admin

from new_app import models
from django.contrib import admin
from .models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)