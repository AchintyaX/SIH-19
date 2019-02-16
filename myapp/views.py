from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.utils import timezone
from .forms import OrderForm

# Create your views here.
def order_list(request):
    orders = Order.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render( request, 'myapp/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'myapp/order_detail.html', {'order': order})

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