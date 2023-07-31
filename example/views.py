from django.shortcuts import render
from example.models import Account

# Create your views here.
def getDataAccount():
    ga = Account.objects.using('example').filter(customer_number='1001')
    print(ga.values())
