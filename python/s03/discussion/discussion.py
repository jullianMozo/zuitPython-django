# several structure to store collection or multiple item in a single variable


# List
# List is similar to array in JS in a sense they contain a collection of data
# to create a list, the [] bracket is used

names = ["rowie", "erricson", "Laira", "paolo", "richmore"]
programs = ["developer career", "short courses", 
            "free codding bootcamp"]
duration = [260, 180, 20]
truth_values = [True, False, True, True, False]

print(names)
print(programs)
print(duration)
print(truth_values)

sample_list = ["apple", 3, False, "potato", 4]
print(sample_list)

# getting the list size 
# the  number of element in a list can be counted using 
# the len() method

print(len(programs))

# accessing values of list
# List can be access by providing the index number of element
# the index start at 0 and  ends at n-1 where n is the number of elements

# access the first item in the list
print(programs[0])
# access the last item in the list
print(programs[-1])
# access whole list
print(duration)

# access range of values
# list[start index: end index]
#  start index - included
# end index - to be exclided
print(programs[0:2])

# mini activity 1


student_names = ["john", "jane", "mathew", "mary", "simon"]
student_grade = [99,98,97,95,96]

# for name, grade in zip(student_names, student_grade):
#     print(f"The grade of {name} is {grade}")

count = 0
while count < len(student_names):
    print(f"The grade of {student_names[count]} is {student_grade[count]}")
    count += 1

# updating list
# print the current value
print(f"Current value: {programs[1]}")
# update the values
programs[1] = "short courses"
# print new value
print(f"new value: {programs[1]}") 

# list Manipulation
# list has methods that can be used to manipulate the element within
# adding list of items - the append() method allows insert items to the list

programs.append("global")
print(programs)

# deleteing items in the list - del keyword is used to delete items in the list
duration.append(360)
print(duration)

del duration[-1]
print(duration)

# membership checks - the in keyword checks if the elements in the list
# return true or false

print(20 in duration)
print(500 in duration)

# sorying list - the sort() method is used to sort the list
# alphanumerically, ascending by default

print(names)
names.sort()
print(names)

# emptying the list - clear() method is used to empty the content of the list

test_list = [1,2,3,4,5]
print(test_list)
test_list.clear()
print(test_list)

# dictionaries - are used to store data values in key:value pair
# similar to obeject in JS.

person1 = {
    "name": "brandon",
    "age": 28,
    "occupation": "student",
    "isEnrolled" : True,
    "subject": ["python", "SQL", "Django"]
} 

# to get the number of key-pairs in the dictionary
# len() method can be used

print(len(person1))

# accessing the values in the dictionary
print(person1["name"])

# keys method - will return a list of all the keys in the dictionary
print(person1.keys())

# values method - will return all the values in th dictionary
print(person1.values())

# items() method - will return item in a dictionary as a key value pair in list
print(person1.items())


# adding key value pairs
#  1. putting a new index and assing values
person1["nationality"] = "filipino"
#  2. using update method
person1.update({"fav_food": "sinigang"})
print(person1)

# deleting entries can be done by using pop() method or del keyword
person1.pop("fav_food")
del person1["nationality"]
print(person1)

# clear() method emties ditionary
person2 ={
    "name": "john",
    "age": 18
}
print(person2)
person2.clear()
print(person2)

# looping through dictionaries
for key in person1:
    print(f"The value of {key} is {person1[key]}")


# nested dictionary
person3 = {
    "name": "monika",
    "age": 20,
    "occupation": "poet",
    "isEnrolled": True,
    "subjects": ["pythom", "SQL", "Django"]
}     

classroom = {
    "student1": person1,
    "student2": person3
}

print(classroom)


# mini activity 2
car = {
    "brand" : "toyota",
    "model": "hilux",
    "year": "2024",
    "color": "metalic gray"
}
print(f"I own {car['brand']} {car['model']} and it was made in {car['year']}")

# function - are blocks of code thats run when called

# The def keyword use to create a function the syntax is
# def <function_name>()


# defines a function called my greeting
def my_greeting():
    # code to be run when my_greeting is called
    print("hello user")

# calling or invoking a function
my_greeting()


def greet_user(username):
    print(f"Hello, {username}!")
greet_user("bob")
greet_user("amy")

# return statement - the return keyword allow function to return a value

def addition(num1, num2):
    return num1 + num2
sum = addition (5,10)
print(f"the sum is {sum}")

# lambda function
# a lambda function is a small anonymous function that ca be used for callback

greeting = lambda person : f"hello {person}"
print(greeting("elsie"))
print(greeting("anthony"))

mult = lambda a,b : a*b
print(mult(5,6))
print(mult(9,15))

#  mini activity 3 
# create a function that gets a square of a number


def square(num):
    return num ** 2
result = square(5)
print(f"the square of number is {result}")

#  Classes
# classes would serve as a bluprint to describe the concept of object
# ClassName()

class Car():
    def __init__(self, brand, model, year_of_make):
        self.brand = brand
        self.model = model
        self.year_of_make = year_of_make

        self.fuel = "gasoline"
        self.fuel_level = 0

        # methods
    def fill_fuel(self):
        print(f"current fuel level: {self.fuel_level}")
        print("fill up the fuel tank")
        self.fuel_level = 100
        print(f"New fuel level: {self.fuel_level}")

       

# create a new instance
new_car = Car("nissan", "GTR", "2019")
print(f"my car is a {new_car.brand} {new_car.model}")

new_car.fill_fuel()


