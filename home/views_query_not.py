from home.models import Loan, Invoice
from django.db.models import Q

#NOT using .exclude()
def queryExclude():
    data = Invoice.objects.exclude(principal_amout__in=[200,300])
    print(data.query)
    print(" === ==== ==== ===")
    print(data.values())
    
def queryQ():
    data = Invoice.objects.filter(~Q(principal_amout__in=[200,300]))
    print(data.query)
    print(" === ==== ==== ===")
    print(data.values())
