from home.models import Loan
from django.db.models import Q

def selectDataByLikeAndNot():
    sla = Loan.objects.filter(
        Q(product_name__startswith='P') & ~Q(product_name__startswith='T')
    )
    
    print(sla.query)
    print("=== ==== ====")
    print(sla.values())