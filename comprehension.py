''' Comprehension
    (1) Wat is comprehension & list comp.
    (2) set and dicionary comp.
'''

print("====== Wat is comprehension & list comp ======")
# Comprehension boshqa tillardagi spread operatori 

''' Comprehension
    a) *iterable
    b) <expression> for item in iterable 
    c) <expression> for item in iterable <condition>
'''

#list comp.
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers] # aversion

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("-----------")
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people] # b version
print("list_people:", list_people)


cars = [ 
    ("Ferrari", 78),
    ("Tayota", 87),
    ("'Audi", 116),
    ("BMW", 109),
    ("'Pagani", 33)
]
list_cars = [car[0] for car in cars if car[1] > 80] #c version
print("list_cars:", list_cars)
