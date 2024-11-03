from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self, food):
        pass
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__()
        self._name = name
        self._breed = breed 
        self._age = age


    def eat(self, food):
        print(f"{self._name} is eating {food}.")

    def make_sound(self):
        print("Meow! Nyaw! Nyaaa!")    

    # getter method of cat
    def get_name(self):
        print(f"The cat name is {self._name}")
    def get_breed(self):
        print(f"breed of the cat is {self._breed}")
    def get_age(self):
        print(f"the age of the cat is {self._age}")

    # setter of method cat 

    def set_name(self, name):
        self._name =  name
    def set_breed(self, breed):
        self._breed = breed
    def set_age(self, age):
        self._age = age
    def call(self):
        print(f"{self._name} come on") 




class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__()
        self._name = name
        self._breed = breed 
        self._age = age


    def eat(self, food):
        print(f"{self._name} is eating {food}.")

    def make_sound(self):
        print("Bark! Woof! Arf!")

    # getter method of cat
    def get_name(self):
        print(f"The dog name is {self._name}")
    def get_breed(self):
        print(f"breed of the dog is {self._breed}")
    def get_age(self):
        print(f"the age of the dog is {self._age}")

    # setter of method cat 

    def set_name(self, name):
        self._name =  name
    def set_breed(self, breed):
        self._breed = breed
    def set_age(self, age):
        self._age = age

    def call(self):
        print(f"{self._name} come on")    


dog1 = Dog("Isis", "dalamtian", 15)
dog1.eat("steak")
dog1.make_sound()
dog1.call()
cat1 = Cat("Isis", "dalamtian", 15)
cat1.eat("Tuna")
cat1.make_sound()
cat1.call()

  
            
