'''LOOP operators
(1) for
(2) break/else
(3) while
'''

print("====== for operators ======")
# Iterable object > string dict tuple list range map filter(function, iterable) takrorlanish hususiyatiga ega bo'lgan obj

text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)  # [0, 5]

for letter in text:
    print(f"The letter: {letter}")

print("----------")
for number in numbs:
    print(f"The number: {number}")

print("----------")
for key in car_obj:
    print(f"The key: {key} => value: {car_obj.get(key)}")


print("====== break/else ======")
for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("Reached break")
        break
else:
    print("Executed succesfully")


print("====== while operator ======")

numb = 40
while numb > 0:
    numb -= 10
    print(f"the numb equals {numb}")


print("----------")
count = 0
while True:
    count += 1
    x = int(input("Find number"))
    
    
    if x == 41:
        print(f"You found number in {count} steps")
        break
    else:
        print("Wrong, please find again!")
    
    
