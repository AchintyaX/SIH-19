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
    Reason_delay = models.TextField(null=True, blank=True)
    order_details = models.TextField(null= True)
    delay = models.DecimalField( blank=True, null=True, decimal_places=0, max_digits=2)
    order_status = models.CharField( max_length=2, choices=ORDER_STATUS, default=APPROVED)

    def publish(self):
        self.save()

    def __str__(self):
        return self.clientName

class Supplier(models.Model):
    supplier_id = models.CharField(max_length=10, null=False)
    supplier_name = models.CharField(max_length=200 )
    supplier_address = models.TextField()
    supplier_email = models.EmailField()
    supplier_time = models.IntegerField(default=10)
    supplier_delay = models.BooleanField(default=False)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.supplier_name

class Product(models.Model):
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


    A = 'A'
    B = 'B'
    C = 'C'

    PRODUCT_TYPE  = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
    )

    supplier = models.ForeignKey('myapp.Supplier', on_delete=models.CASCADE, related_name='products')
    order_id = models.CharField(max_length=10, null=False)
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE, default=A)
    main_order_date = models.DateTimeField(default=timezone.now)
    completion_date = models.DateField()
    recieved_date = models.DateField()
    product_status = models.CharField(max_length=2, choices=ORDER_STATUS, default=APPROVED)
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.order_id

class Raw(models.Model):
    NOUPDATE = 'NA'
    PROCESSING = 'PR'
    ACQUIRED = 'AQ' 
    UTILIZING = 'UT'
    ORDER_STATUS = (
        (NOUPDATE, 'NoUpdate'),
        (PROCESSING, 'Processing'),
        (ACQUIRED, 'Acquired'), 
        (UTILIZING, 'Utilizing'), 

    )
    A = 'A'
    B = 'B'
    C = 'C'

    PRODUCT_TYPE  = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
    )

    supplier= models.ForeignKey('myapp.Supplier', on_delete=models.CASCADE, related_name='raws')
    mill_name = models.CharField(max_length=200)
    component_type = models.CharField(max_length=1, choices=PRODUCT_TYPE, default=A)
    component_status = models.CharField(max_length=2, choices=ORDER_STATUS, default=NOUPDATE)
    lead_time = models.IntegerField(default=2)

    def publish(self):
        self.save()
    def __str__(self):
        return self.mill_name