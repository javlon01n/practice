''' CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE
(3) POLIMORPHISM
'''

print("===== INHERITENCE =====")
# PARENT > CHILD parent uzini childiga public hamda protected (state + methodlarini) uzatadi


class Animal:  # PARENT
    # state
    description = "The class is parent for animals"

    # constructor
    def __init__(self, voise):
        self._status = "animal is alive"
        self.voise = voise

    # method

    def make_voise(self):
        print(f"the animal can make voice: {self.voise}")


class Dog(Animal):  # child
    # state

    # constructor

    def __init__(self, name, sound, voise):
        self.name = name
        self.sound = sound
        super().__init__(voise)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, i can protect you!")

    def make_voise(self):
        print(f"the {self.name} says {self.sound}")



class Cat(Animal):  # child
    # state

    # constructor

    def __init__(self, name, sound, voise):
        self.name = name
        self.sound = sound
        super().__init__(voise)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        pass


class Fish(Animal):  # child
    # state

    # constructor

    def __init__(self, name, sound, voise):
        self.name = name
        self.sound = sound
        super().__init__(voise)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes i can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "zZz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-----------")
dog.make_voise()
fish.make_voise()

print(Animal.description)
print(Dog.description)

print(dog.voise, fish.voise)
print("dog.status:", dog._status)
print("cat.status:", cat._status)


print("===== POLIMORPHISM =====")

dog.make_voise()
fish.make_voise()

print("______")
# fish >Fish Animal > object()
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
