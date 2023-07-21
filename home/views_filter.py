from home.models import Loan


#filter using AND

def filterAnd():
    #select * from loan where id=2 and tenor_pinjama=30
    fAnd = Loan.objects.filter(id=2, tenor_pinjaman=30)
    print(fAnd.query)
    print(fAnd.values())
    
def filterOr1():
    fOrd = Loan.objects.filter(tenor_pinjaman=30) | Loan.objects.filter(tenor_pinjaman=7)
    print(fOrd.query)
    print(fOrd.values())
    
def filterOr2():
    from django.db.models import Q
    fOrd = Loan.objects.filter(Q(tenor_pinjaman=30) | Q(tenor_pinjaman=7))
    print(fOrd.query)
    print(fOrd.values())
    
#select * from borrower_loan where product_name like '%berjangka%'

def filterContains():
    fCont = Loan.objects.filter(product_name__contains='BERJANGKA')
    print(fCont.query)
    print(fCont.values())
    
def filterIcontains():
    fCont = Loan.objects.filter(product_name__icontains='BERJANGKA')
    print(fCont.query)
    print(fCont.values())
    
#where like product_name 'P%'
def filterStartWith():
    fCont = Loan.objects.filter(product_name__startswith='P')
    print(fCont.query)
    print(fCont.values())

def filterIStartsWith():
    fCont = Loan.objects.filter(product_name__istartswith='p')
    print(fCont.query)
    print(fCont.values())
    
    
#where like product_name '%ngka'
def filterEndsWith():
    fCont = Loan.objects.filter(product_name__endswith='NGKA')
    print(fCont.query)
    print(fCont.values())

def filterIEndsWith():
    fCont = Loan.objects.filter(product_name__iendswith='NGKA')
    print(fCont.query)
    print(fCont.values())

