from home.models import Loan, Invoice
from datetime import date

def insertTblForeignKey1():
    inv = Invoice(
        Loan_id = 3,
        tgl_invoice = date.today(),
        principal_amout = 1000.00
    )
    inv.save()

def insertTblForeignkey2():
    getLoan = Loan.objects.get(id=2)
    inv = Invoice(
        Loan = getLoan,
        tgl_invoice = date.today(),
        principal_amout = 1000.00
    )
    inv.save()
    
def insertTblForeignKey3():
    getLoan = Loan.objects.all()
    for x in getLoan:
        inv = Invoice(
            Loan = x,
            tgl_invoice = date.today(),
            principal_amout = 300.00
        )
        inv.save()