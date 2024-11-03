#  python class review

class SampleClass():
    def __init__(self, year):
        self.year = year

    def show_year(self):
        print(f"This year is: {self.year}")

myObj = SampleClass(2024)
print(myObj.year)
myObj.show_year()




#  Fundamentals of OOP
#  Encapsulation - is a mechanisim of wrapping the attributed and code
# acting on the methods together as a single unit
 

class Person():
    def __init__(self):
        self._name = "john doe"
        self._age = 0
# setter method / modify
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age
        
# getter method / viewing
    def get_name(self):
        print(f"Name of person : {self._name}")

    def get_age(self):
        print(f"The output for get_age(): {self._age}") 


p1 = Person()
# print(p1._name)  
p1.get_name()
p1.set_name("bob doe")
p1.get_name() 
p1.set_age(18)
p1.get_age()

# Mini activity 1

# add another protected attribute called age and create the neccessary
# getter and setter methods



# INHERITANCE

# the transfer of the characteristice of a class to other classes 
# rthat are derived from it

# to create am inheritance class in the classname definition
# add parent class

# child or subclass

class Employee(Person):
    def __init__(self, employeeId):
        super().__init__()
        # attribute that is unique to emplyee class
        self._employeeId = employeeId

     # method of employee class    
    def get_employeeId(self):
        print(f"The employee ID is {self._employeeId}")

    # setter method of employee id
    def set_emplotyeeId(self, employeeId):
        self._employeeId = employeeId

    # details method
    def get_details(self):
        print(f"{self._employeeId} belongs to {self._name}") 


empl = Employee("Emp-001")
empl.get_details()
empl.set_name("jane doe")
empl.set_age(20)
empl.get_details()

# Mini-Activity 2: 6:40PM
# Create a new class called Student that inherits Person with the additional attributes

# Attributes: student_no, course, year_level
# Methods: get_details: Print the output
# <Student Name> is currently in year <year level> taking up <course>
# necessary getter and setters


class Student(Person):
    def __init__(self, student_no, course, year_level):
        super().__init__()
        self._student_no = student_no
        self._course = course
        self._year_level = year_level

    # getter method of student class    
    def get_student_no(self):
        print(f"student number is  {self._student_no}")
    def get_course(self):
        print(f"course number is  {self._course}")
    def get_year_level(self):
        print(f"year level number is  {self._year_level}")

    # setter method of employee id
    def set_student_no(self, student_no):
        self._student_no = student_no
    def set_course(self, course):
        self._course = course
    def set_year_level(self, year_level):
        self._year_level = year_level

    # costum method
    def get_details(self):
        print(f"{self._name} in currently in year{self._year_level} taking up {self._course}") 


# Test Cases:
student1 = Student("stdt-001", "Computer Science", 4)
student1.get_details()

        
# POLYmmorphism
# 
# A child class inherits all the methods from the parent clss
# however in some situation the methods inherited form the parent doesnt quite
# fit into the child class. In such case we will have to reimpliment the method


class Admin():
    def is_admin(self):
        print(True)

    def user_type(self):
        print("admin is user")


class Customer():
    def is_admin(self):
        print(False)

    def user_type(self):
        print("regular user")

def test_funtion(obj):
    obj.is_admin()
    obj.user_type()


user_admin = Admin()
user_customer = Customer()

test_funtion(user_admin)
test_funtion(user_customer)
                




# Polymorphism with Class methods:
class TeamLead():
	def occupation(self):
		print("Team Lead")

	def has_auth(self):
		print(True)

class TeamMember():
	def occupation(self):
		print("Team Member")

	def has_auth(self):
		print(False)

tl1 = TeamLead()
tm1 = TeamMember()

for person in (tl1, tm1):
	# access the occupation method of each item
	person.occupation()                



# plymoriphism with inheritance
# method Overriding

class zuitt():
     def tracks(self):
          print(f"we are currently offering 3 tracks(developer career, pi shape career, short courses)")


     def num_of_hours(self):
          print(f"learn web development in 360hrs")

class DeveloperCareer(zuitt):
     def num_of_hours(self):
          print(f"learn the basics of web developement in 240 hrs")

class PiShapeCareer(zuitt):
     def num_of_hours(self):
          print(f"learn skills for no code in 140 hrs")

class ShortCourses(zuitt):
     def num_of_hours(self):
          print(f"learn advance topics in web developement in 20 hrs")


course1 = DeveloperCareer()
course2 = PiShapeCareer()
course3 = ShortCourses() 

course1.num_of_hours()
course2.num_of_hours()
course3.num_of_hours()


# Abstraction 

from abc import ABC, abstractclassmethod

class Polygon(ABC):
     @abstractclassmethod
     def printNumberOfSides(self):
        #   pass keyword denotes that the method doesnt do anything
          pass
     
class Triangle(Polygon):
     def __init__(self):
          super().__init__()

     def printNumberOfSides(self):
        print("this polygon has 3 sides")          

class Pentagon(Polygon):
     def __init__(self):
          super().__init__()

     def printNumberOfSides(self):
        print("this polygon has 5 sides")



shape1 = Triangle()
shape2 = Pentagon()
shape1.printNumberOfSides()
shape2.printNumberOfSides()  


          
                  