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
    
#where tenor_pinjaman in (70,30)
def filterByIn():
    fIn = Loan.objects.filter(tenor_pinjaman__in = [7,30])
    print(fIn.query)
    print("=== === ====")
    print(fIn.values())
    
#where tenor_pinjaman < 30
def filterByLt():
    fLt = Loan.objects.filter(tenor_pinjaman__lt = 30)
    print(fLt.query)
    print("=== === ====")
    print(fLt.values())
    
#where tenor_pinjaman <= 30
def filterByLte():
    fLt = Loan.objects.filter(tenor_pinjaman__lte = 30)
    print(fLt.query)
    print("=== === ====")
    print(fLt.values())
    
#where tenor_pinjaman > 7
def filterGt():
    fgt = Loan.objects.filter(tenor_pinjaman__gt = 7)
    print(fgt.query)
    print("=== === ====")
    print(fgt.values())
    
#where tenor_pinjaman >= 7
def filterGte():
    fgt = Loan.objects.filter(tenor_pinjaman__gte = 7)
    print(fgt.query)
    print("=== === ====")
    print(fgt.values())
    
#where tenor_pinjaman between 5 and 45
def filterByRange():
    fgt = Loan.objects.filter(tenor_pinjaman__range = (5, 45))
    print(fgt.query)
    print("=== === ====")
    print(fgt.values())

