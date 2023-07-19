from django.db import models
from utils.models import CreateUpdate

# Create your models here.

#table name = Borrower_loan
class Loan(CreateUpdate):
    product_name = models.CharField(max_length=55)
    penor_pinjaman = models.IntegerField(default=0)
    anggal_publish = models.DateTimeField(blank=True, null=True)
        
    class Meta:
        db_table = "borrower_loan"
