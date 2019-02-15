from django.shortcuts import render, get_object_or_404
from .models import Order
from django.utils import timezone

# Create your views here.
def order_list(request):
    orders = Order.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render( request, 'myapp/order_list.html', {'orders': orders})
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'myapp/order_detail.html', {'order': order})
