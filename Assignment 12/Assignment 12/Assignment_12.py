# assignment 12 weee
class Employee:
    def __init__(self, name="", idNumber=0, department="", position=""):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position

    # mutator
    def set_name(self, name):
        self.name = name

    def set_idNumber(self, idNumber):
        self.idNumber = idNumber

    def set_department(self, department):
        self.department = department

    def set_position(self, position):
        self.position = position

    # accessor
    def get_name(self):
        return self.name

    def get_idNumber(self):
        return self.idNumber

    def get_department(self):
        return self.department

    def get_position(self):
        return self.position


# creat employee
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# display
employees = [employee1, employee2, employee3]

for employee in employees:
    print("Name:", employee.get_name())
    print("ID Number:", employee.get_idNumber())
    print("Department:", employee.get_department())
    print("Position:", employee.get_position())
    print()


   # this is second question
class Patient:
    def __init__(self, first, middle, last, address, city, state, zip,
                 phone, emergencyName, emergencyPhone):
        self.first = first
        self.middle = middle
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.emergencyName = emergencyName
        self.emergencyPhone = emergencyPhone

    # accessor
    def get_first(self):
        return self.first

    def get_middle(self):
        return self.middle

    def get_last(self):
        return self.last

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    def get_phone(self):
        return self.phone

    def get_emergencyName(self):
        return self.emergencyName

    def get_emergencyPhone(self):
        return self.emergencyPhone


class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    # accessor 
    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_practitioner(self):
        return self.practitioner

    def get_charge(self):
        return self.charge


# the actual patient
patient = Patient(
    "John",
    "Jane",
    "Smith",
    "123 Placeholder Street",
    "Chicago",
    "IL",
    "60600",
    "555-123-4567",
    "Jane Smith",
    "555-987-6543"
)

# create objects
procedure1 = Procedure("Physical Exam", "Today's date", "Dr. Irvine", 250.00)
procedure2 = Procedure("X-ray", "Today's date", "Dr. Jamison", 500.00)
procedure3 = Procedure("Blood test", "Today's date", "Dr. Smith", 200.00)

# display
print("Patient Information")
print()
print("Name:", patient.get_first(), patient.get_middle(), patient.get_last())
print("Address:", patient.get_address())
print("City:", patient.get_city())
print("State:", patient.get_state())
print("ZIP Code:", patient.get_zip())
print("Phone:", patient.get_phone())
print("Emergency Contact:", patient.get_emergencyName())
print("Emergency Phone:", patient.get_emergencyPhone())

# display procedure
print("\nProcedure Information")
print()

procedures = [procedure1, procedure2, procedure3]

for procedure in procedures:
    print("Procedure name:", procedure.get_name())
    print("Date:", procedure.get_date())
    print("Practitioner:", procedure.get_practitioner())
    print("Charge: $", format(procedure.get_charge(), ".2f"))
    print()

# totals
total = (procedure1.get_charge() +
         procedure2.get_charge() +
         procedure3.get_charge())

print("Total Charges: $", format(total, ".2f"))
