from home.models import Invoice

def slicingData():
    #select * from borrower_loan_invoice limit 5
    sinvoice = Invoice.objects.all()[:5]
    print(sinvoice.query)
    print(" ==== ===== ===")
    print(sinvoice.values())
    
def slicingDataUseOrderBy():
    sinvoice = Invoice.objects.all().order_by('-id')[:5]
    print(sinvoice.query)
    print(" ==== ===== ===")
    print(sinvoice.values('id','principal_amount'))
    
# [:5] limit
# [offset:offset+limit] -> [5:10]

def slicingDataUseOffset():
    #select * from borrower_loan_invoice limit 5 offset 5
    sinvoice = Invoice.objects.all()[5:10]
    print(sinvoice.query)
    print(" ==== ===== ===")
    print(sinvoice.values('id','principal_amount'))