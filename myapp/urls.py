from django.urls import path
from . import views

# setting the url patterns 

urlpatterns =[
    path('', views.order_list, name='order_list'),
]