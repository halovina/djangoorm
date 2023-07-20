from django.db import models
from utils.models import CreateUpdate

# Create your models here.

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
    principal_amout = models.FloatField(default=0.0)
    
    class Meta:
        db_table = "borrower_loan_invoice"
