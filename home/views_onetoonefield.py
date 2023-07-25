from home.models import Contact, Customers


def createCustomer():
    print("start1 ====")
    ctk = Contact(
        phone = "0834567900000",
        address = "Jl Raya Sawo Jajar"
    )
    ctk.save()
    
    print("start2 =====")
    cust = Customers(
        firstname = "Amah",
        lastname = "Safira",
        contact = ctk
    )
    cust.save()
    print("sukses =====")
    
def createCustomerByExistingContact():
    ctk = Contact.objects.get(id=1)
    cust = Customers(
        firstname = "Amah2",
        lastname = "Safira2",
        contact = ctk
    )
    cust.save()
    