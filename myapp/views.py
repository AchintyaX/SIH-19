from django.shortcuts import render
from .models import Order
from django.utils import timezone

# Create your views here.
def order_list(request):
    orders = Post.objects.filter(completion_date__lte=timezone.now()).order_by('completion_date')
    return render( request, 'myapp/order_list.html', {'orders': orders})
