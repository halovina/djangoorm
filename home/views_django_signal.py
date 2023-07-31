# https://docs.djangoproject.com/en/4.2/ref/signals/

# Django Built-in Signals
#     pre_init
#     post_init
#     pre_save
#     post_save
#     pre_delete
#     post_delete
#     m2m_changed

from home.models import Event, Employee
from datetime import datetime

def createNewEvent():
    gte = Employee.objects.get(id=1)
    ev = Event(
        event_name = "Belajar programing gratis {}".format(str(datetime.now())),
        location = "JL Margono 123456",
        employee = gte
    )
    ev.save()