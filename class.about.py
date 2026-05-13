''' CLASS
    (1) What is class
    (2) ordinary vs static properties
    (3) special methods
'''

print("===== What is class =====")
# classlar object yasovchi shablon
# classlar 3xil turdagi strukturaga ega > state constructor method


class Person():
    # state
    message = "static state property"

# constructor

    def __init__(self, name, age):  # self bu this
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed!")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("Jhon", 22)

# odatiy state
print("person1.name", person1.name)

# odatiy method
person1.introduce()
person2.say_age()


print("===== ordinary vs static properties =====")
# static state

new_message = Person.message
print("new_message", new_message)

# static method
Person.explain()


print("===== special methods =====")
# Pythonning eng ko'p ishlatiladigan methodlari
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...add()


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

        # method
    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"The {self.name} stoped engine!")
        
        
    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"
    
    def __call__(self):
        print("Object called as function!")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("-------")
your_car = Car("Tayota", 2026)
print(your_car)
response = your_car() #CALL 
print("response", response)