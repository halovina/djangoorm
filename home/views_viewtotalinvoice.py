from home.models import ViewTableTotalInvoice

def getDataViewTable():
    gv = ViewTableTotalInvoice.objects.all()
    print(gv.values())