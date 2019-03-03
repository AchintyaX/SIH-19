from django.urls import path, include
from . import views
  
# setting the url patterns 

urlpatterns =[
    path('', views.home, name='home'),
    path('supplierlist/', views.supplier_list, name='supplier_list' ),
    path('supplier/<int:pk>/', views.supplier_detail, name='supplier_detail' ),
    path('order/new/', views.order_new, name='order_new'), 
    path('order/<int:pk>/edit', views.order_edit, name='order_edit'), 
    path('supplier/<int:pk>/product/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit', views.product_edit, name='product_edit'),
]