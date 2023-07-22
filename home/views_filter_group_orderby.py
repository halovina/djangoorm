from home.models import Loan, Invoice
from django.db.models import Count

def filterOrderBy():
    flt = Invoice.objects.all().order_by('-id')
    print(flt.query)
    print("=== ==== ====")
    print(flt.values())
    
def queryGroupBy():
    qb = Invoice.objects.values('principal_amout').annotate(pAcount=Count('principal_amout')).order_by('-principal_amout')
    print(qb.query)
    print(" ==== ===== ===")
    print(qb)