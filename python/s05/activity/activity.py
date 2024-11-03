# Abstract Person class
from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def getFullName(self):
        pass

    def addRequest(self):
        return "Request has been added"

    def checkRequest(self):
        pass

    def addUser(self):
        pass


# Employee class inheriting from Person
class Employee(Person):
    def __init__(self, firstName, lastName, email, department):
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._department = department

    # Getter methods
    def get_firstName(self):
        return self._firstName

    def get_lastName(self):
        return self._lastName

    def get_email(self):
        return self._email

    def get_department(self):
        return self._department

    # Setter methods
    def set_firstName(self, firstName):
        self._firstName = firstName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def set_email(self, email):
        self._email = email

    def set_department(self, department):
        self._department = department

    # Custom methods
    def getFullName(self):
        return f"{self._firstName} {self._lastName}"

    def login(self):
        return f"{self._email} has logged in"

    def logout(self):
        return f"{self._email} has logged out"


# TeamLead class inheriting from Person
class TeamLead(Person):
    def __init__(self, firstName, lastName, email, department):
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._department = department
        self.members = []

    # Custom methods
    def getFullName(self):
        return f"{self._firstName} {self._lastName}"

    def login(self):
        return f"{self._email} has logged in"

    def logout(self):
        return f"{self._email} has logged out"

    def addMember(self, employee):
        self.members.append(employee)
        return f"{employee.getFullName()} has been added to the team."

    def get_members(self):
        return self.members


# Admin class inheriting from Person
class Admin(Person):
    def __init__(self, firstName, lastName, email, department):
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._department = department

    # Custom methods
    def getFullName(self):
        return f"{self._firstName} {self._lastName}"

    def login(self):
        return f"{self._email} has logged in"

    def logout(self):
        return f"{self._email} has logged out"

    def addUser(self):
        return "user has been added!"


# Request class to handle ticketing
class Request():
    def __init__(self, name, requester, dateRequested, status="open"):
        self._name = name
        self._requester = requester
        self._dateRequested = dateRequested
        self._status = status

    # Getter methods
    def get_name(self):
        return self._name

    def get_requester(self):
        return self._requester

    def get_dateRequested(self):
        return self._dateRequested

    def get_status(self):
        return self._status

    # Setter methods
    def set_status(self, status):
        self._status = status
        return f"Request {self._name} has been updated to {self._status}"

    def closeRequest(self):
        self._status = "closed"
        return f"Request {self._name} has been closed."

    def cancelRequest(self):
        self._status = "cancelled"
        return f"Request {self._name} has been cancelled."


# Testing the system

# Creating objects
employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing")
employee2 = Employee("Jane", "Smith", "sjane@mail.com", "Marketing")
employee3 = Employee("Robert", "Patterson", "probert@mail.com", "Sales")
employee4 = Employee("Brandon", "Smith", "sbrandon@mail.com", "Sales")
admin1 = Admin("Monika", "Justin", "jmonika@mail.com", "Marketing")
teamLead1 = TeamLead("Michael", "Specter", "smichael@mail.com", "Sales")
req1 = Request("New hire orientation", teamLead1, "27-Jul-2021")
req2 = Request("Laptop repair", employee1, "1-Jul-2021")

assert employee1.getFullName() == "John Doe", "Full name should be John Doe"
assert admin1.getFullName() == "Monika Justin", "Full name should be Monika Justin"
assert teamLead1.getFullName() == "Michael Specter", "Full name should be Michael Specter"
assert employee2.login() == "sjane@mail.com has logged in"
assert employee2.addRequest() == "Request has been added", "Request message should be static"
assert employee2.logout() == "sjane@mail.com has logged out"

teamLead1.addMember(employee3)
teamLead1.addMember(employee4)
for indiv_emp in teamLead1.get_members():
    print(indiv_emp.getFullName())

assert admin1.addUser() == "user has been added!"

req2.set_status("closed")
print(req2.closeRequest())
