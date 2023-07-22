from home.models import Loan, Invoice

def joinWithIn():
    jointb = Invoice.objects.filter(Loan__tenor_pinjaman__in = [7,30])
    print(jointb.query)
    print(" === ===== =====")
    print(jointb.values())
    
def joinWithContain():
    jointb = Invoice.objects.filter(Loan__product_name__contains = "tenor")
    print(jointb.query)
    print(" === ===== =====")
    print(jointb.values())