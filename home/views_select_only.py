from home.models import Loan, Invoice

#select * from borrower_loan_invoice

#.values -> select Loan_id, principal_amout, tgl_invoice from borrower_loan_invoice where 
def selUsingVlues():
    slv = Invoice.objects.filter(principal_amount__in = [200,300]).values('Loan_id','principal_amount', 'tgl_invoice')
    print(slv.query)
    print("=== ==== ===")
    print(slv)



#.only
def selUsingOnly():
    slv = Invoice.objects.filter(principal_amount__in = [200,300]).only('Loan_id','principal_amount', 'tgl_invoice')
    print(slv.query)
    print("=== ==== ===")
    for x in slv:
        print("loan id: {}".format(x.Loan_id))
        print("principal_amount: {}".format(x.principal_amount))
        print("tgl_invoice: {}".format(x.tgl_invoice))
        print("==========")