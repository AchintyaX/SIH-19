from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Supplier
from django.utils import timezone
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render( request, 'myapp/home.html')
@login_required
def supplier_list (request):
    suppliers = Supplier.objects.all()
    return render( request, 'myapp/supplier_list.html', {'suppliers': suppliers})
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