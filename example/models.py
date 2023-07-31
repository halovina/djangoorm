from django.db import models

# Create your models here.
class Account(models.Model):
    account_number = models.CharField(max_length=15)
    customer_number = models.CharField(max_length=15)
    customer_number = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'accounts'