from django import forms
from .models import Order, Supplier, Product
from django.utils import timezone

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('OrderID','clientName', 'start_date', 'completion_date', 'order_details', 'Reason_delay',)

class UpdateOrderForm(forms.Form):
    APPROVED = 'AP'
    PROCESSING = 'PR'
    PACKED = 'PD'
    DISPATCHED = 'DP'
    ORDER_STATUS = (
        (APPROVED, 'Approved'),
        (PROCESSING, 'Processing'),
        (PACKED, 'Packed'), 
        (DISPATCHED, 'Dispatched'), 

    )

    OrderID = forms.IntegerField()
    clientName = forms.CharField( max_length=20)
    start_date = forms.DateField(initial=timezone.now())
    completion_date = forms.DateField(widget=forms.SelectDateWidget(
        
    ))
    order_details = forms.CharField()
    Reason_delay = forms.CharField()
    order_status = forms.CharField( max_length=2)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('order_id', 'product_type', 'main_order_date', 'completion_date', 'recieved_date','product_status')