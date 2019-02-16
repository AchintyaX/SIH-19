from django.urls import path
from . import views

# setting the url patterns 

urlpatterns =[
    path('', views.order_list, name='order_list'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('order/new/', views.order_new, name='order_new'), 
    path('order/<int:pk>/edit', views.order_edit, name='order_edit'), 
]