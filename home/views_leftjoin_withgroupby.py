from home.models import Loan
from django.db.models import Count

def getLeftJoin():
    sloan = Loan.objects.filter(
        loan_invoice__isnull=False
    )
    print(sloan.query)
    print("=== ==== ====")
    print(sloan.values())

def getLeftJoinWithGroupBy():
    sloan = Loan.objects.values('product_name').annotate(
        total_invoice = Count('loan_invoice')
    ).filter(total_invoice__gt=5)
    print(sloan.query)
    print("=== ==== ====")
    print(sloan.values('product_name', 'total_invoice'))