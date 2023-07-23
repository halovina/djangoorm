from home.models import Loan, Invoice
from django.db.models import OuterRef, Count, Subquery


def sampleSubquery():
    tInvoice = Invoice.objects.filter(
        Loan=OuterRef('pk')
    ).values('Loan_id').annotate(
        totalInvoice = Count('Loan_id')
    )
    
    tLoan = Loan.objects.all().values('id','product_name','tenor_pinjaman').annotate(
        totalInvoice = Subquery(
            tInvoice.values('totalInvoice')
        )
    )
    
    print(tLoan.query)
    print(tLoan)
    