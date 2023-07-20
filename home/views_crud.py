from home.models import Loan
from datetime import datetime


def createLoan():
    crLoan = Loan(
        product_name = "Pinjaman berjangka",
        tenor_pinjaman = 30, #1bulang
        tanggal_publish =  datetime.now()
    )
    crLoan.save()
    
def readAllLoan():
    getAllLoan = Loan.objects.all()
    for x in getAllLoan:
        print("id: {}".format(x.id))
        print("product_name: {}".format(x.product_name))
        print("tenor_pinjaman: {}".format(x.tenor_pinjaman))
        
def updateLoan(idLoan):
    updateLoan = Loan.objects.get(id=idLoan)
    updateLoan.product_name = "Pinjaman tenor 30 hari"
    updateLoan.save()
    
def deleteLoan(id):
    Loan.objects.get(id=id).delete()
    
    
#select * from loan

# getByID = Loan.objects.filter(id=2)
# str(getByID.query)

# getAll = Loan.objects.all()
# str(getAll.query)
