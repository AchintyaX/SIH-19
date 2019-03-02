from django.contrib import admin
from .models import Order, Supplier, Product

# Register your models here.
admin.site.register(Order)
admin.site.register(Supplier)
admin.site.register(Product)