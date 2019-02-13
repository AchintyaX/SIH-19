from django.db import models

#importing libraries 
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Order(models.Model):
    OrderID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clientName = models.CharField(max_length=200)
    start_date = models.DateTimeField( default=timezone.now)
    completion_date = models.DateTimeField( blank=True, null=True)
    Reason_delay = models.TextField()
    delay = models.DecimalField( blank=True, null=True, decimal_places=0, max_digits=2)

    def publish(self):
        self.save()

    def __str__(self):
        return self.clientName