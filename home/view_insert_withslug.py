from home.models import Employee, Event

def createNewEvent():
    gte = Employee.objects.get(id=1)
    ev = Event(
        event_name = "Belajar programing gratis",
        location = "JL Margono 123456",
        employee = gte
    )
    ev.save()