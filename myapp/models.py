from django.db import models

#importing libraries 
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Order(models.Model):
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

    Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    OrderID = models.CharField(max_length=10, null=False)
    clientName = models.CharField(max_length=200)
    start_date = models.DateTimeField( default=timezone.now)
    completion_date = models.DateTimeField( blank=True, null=True)
    Reason_delay = models.TextField(null=True, default="")
    delay = models.DecimalField( blank=True, null=True, decimal_places=0, max_digits=2)
    order_status = models.CharField( max_length=2, choices=ORDER_STATUS, default=APPROVED)

    def publish(self):
        self.save()

    def __str__(self):
        return self.clientName