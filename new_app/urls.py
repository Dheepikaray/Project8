from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.home_view,name='new'),
    path('index',views.adminclick_view,name='index'),
    path('view',views.customer_signup_view,name='view'),

]