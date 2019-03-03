from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Supplier
from django.utils import timezone
from .forms import OrderForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# Create your views here.

def home(request):
    return render( request, 'myapp/home.html')
@login_required
def supplier_list(request):

    
    if request.user.is_superuser:
        suppliers = Supplier.objects.all()
        for supplier in suppliers:
            if supplier.supplier_delay:
                send_mail('delay', 'you order is delayed kindly hurry', 'achintyashankhdhar@gmail.com', ['ashankahriday@gmail.com'], fail_silently=False)          
        return render(request, 'myapp/supplier_list.html', {'suppliers': suppliers})
    else:
        suppliers = Supplier.objects.all()
        user = request.user
        return render(request, 'myapp/supplier_order_list.html', {'suppliers':suppliers,'user':user})
   
       

   
@login_required
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'myapp/supplier_detail.html', {'supplier': supplier})

@login_required
def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.Author = request.user
            order.start_date = timezone.now()
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'myapp/order_new.html', {'form': form})

@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.Author = request.user
            order.start_date = timezone.now()
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'myapp/order_edit.html', {'form': form})
@login_required
def product_new(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.supplier = supplier
            product.save()
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = ProductForm()
    return render(request, 'myapp/product_new.html', {'form': form})

def product_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method=="POST":
        form = ProductForm(request.POST, instance=supplier)
        if form.is_valid():
            product = form.save(commit=False)
            product.supplier = supplier
            product.save()
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = ProductForm()
    return render(request, 'myapp/product_new.html', {'form': form})