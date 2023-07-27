from home.models import Compensation, Employee

def create_compensatioon_employee():
    comp = Compensation(
        name="Bonus Tahunan"
    )
    comp.save()
    
    emp = Employee(
        firstname = "Anisa",
        lastname = "Hapsari",
        contact_id = 1
    )
    emp.save()
    
    emp.compensation.add(comp)
    emp.save()