from home.models import Event, Employee

def isertTblEvent():
    gte = Employee.objects.get(id=1)
    ev = Event(
        event_name = "JAVA JAS DI PUNCAK DIENG",
        location = "Kabupaten wonosobo jawa tangerang",
        employee = gte
    )
    
    ev.save()