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
#animals[0] = "bird"


