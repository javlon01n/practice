''' Tupl
(1) What is tuple: typle vs list
(2) unpacking arguments
(3) zip
'''

print("====== What is tuple: typle vs list ======")
# Java/PHP/NodeJS array deyiladi => Pythonda esa list

# literal
numbs = [3, 5, 1, 2]

# constructor
letters = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# tuple ni biz hechqachon o'zgartiraolmaymiz
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"


# try avoid thse
people = "Andrew", "Jhon"
# shu xolatda yozib ketishxam mumkun lekin biz xar doyim () qavuslarni qo'yib yozamiz
animals = "dog",
animals = ("dog")


print("====== unpacking arguments ======")
groups = ["MIT", "FLEX", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x:{x} and y: {y}")
print("z:", z)  # tuple  list xolatda olib beradi


#  *args > bu taple degani
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total



# CALL 
calculate(1, 7, 2, 3)
print("------")
calculate(0, 2, 300)
print("------")
calculate(5, 7)

print("=======")
# **kwargs > dictionary qiymatni olib beradi


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi I am {kwargs["name"]} and i am {kwargs["age"]} years old!")



#CALL 
introduce(name="Justin", age=28)
introduce(name="Shawn", age=30, single=True)


# *args, **kwargs birga ishlatish
def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)
    
    
# call 
greeting("Hi", True, 10, name="Jhon", age=22) #args argumentlarni olib berayapti kwasgs esa keylarni 



print("====== zip ======")
tuple1 =(1, 2, 3, 4)
tuple2 =('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped:", zipped)
result = list(zipped)
print(f"the result: {result}")
