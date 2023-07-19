from django.db import models
from datetime import datetime

# Create your models here.

class Loan(models.Model):
    product_name = models.CharField(max_length=55)
    penor_pinjaman = models.IntegerField(default=0)
    anggal_publish = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = datetime.now()
        
        self.updated_date = datetime.now()
        super().save(*args, **kwargs)
