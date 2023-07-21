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
    
    


