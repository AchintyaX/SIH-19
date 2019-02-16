from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('OrderID','clientName', 'start_date', 'completion_date', 'order_details', 'Reason_delay',)