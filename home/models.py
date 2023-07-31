from django.db import models
from utils.models import CreateUpdate
from django.utils.text import slugify
import uuid

# Create your models here.
class Contact(CreateUpdate):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255)
    
    class Meta:
        db_table = "contact"
        
class Customers(CreateUpdate):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.OneToOneField(
        Contact,
        related_name="customers_contact",
        on_delete=models.CASCADE
    )
    
    class Meta:
        db_table = "customers"

#table name = Borrower_loan
class Loan(CreateUpdate):
    product_name = models.CharField(max_length=55)
    tenor_pinjaman = models.IntegerField(default=0)
    tanggal_publish = models.DateTimeField(blank=True, null=True)
        
    class Meta:
        db_table = "borrower_loan"
        
class Invoice(CreateUpdate):
    Loan = models.ForeignKey(
        Loan,
        related_name="loan_invoice",
        on_delete=models.PROTECT
    )
    tgl_invoice = models.DateField(blank=True, null=True)
    principal_amount = models.FloatField(default=0.0)
    
    class Meta:
        db_table = "borrower_loan_invoice"
        
        
#table compensation
    #1 compensation bisa dimiliki oleh lebih dari satu employe
class Compensation(CreateUpdate):
    name = models.CharField(max_length=75)
    
    class Meta:
        db_table = "compensation"
#table employe
    #1 enploye bisa juga punya banyak compensation
class Employee(CreateUpdate):
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    contact = models.OneToOneField(
        Contact,
        related_name="employee_contact",
        on_delete=models.CASCADE
    )
    compensation = models.ManyToManyField(
        Compensation,
        related_name="employee_compensation"
    )

    class Meta:
        db_table = "employee"
        
        
class Event(CreateUpdate):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_name = models.CharField(max_length=55)
    location = models.TextField()
    employee = models.ForeignKey(
        Employee,
        related_name='employee_event',
        on_delete= models.PROTECT
    )
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name)
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = "employee_event"
    
