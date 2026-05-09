'''FUNCTIONS
(1) DEFINE VS CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''


print("==== DEFINE vs CALL====")
# python sintaksusi qurib bergan
# functionlarni building functionlar deb ataymiz
# bular print() type()
''' Function bu malum bir mantiqni ishga tushuruvchi kod block
function tuzganda boshqa tillarda {} shu qavusdan foydalanamiz
pythonda esa : shu belgi indentation! dan foydalanamiz
pythonda define qismi bo'sh qolsa pass deb yozib ketish kerak
'''


# DEFINE - Parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"

 # CALL - Argument
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting('Mark')
print("result2:", result2)


print("===== Keyword & define arguments =====")


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


result3 = give_greet(name="Justin", age=28)
print("result3", result3)

result4 = give_greet("Jhon")
print("result4", result4)

print("==== scope ====")
b = 100  # (3)qiymatni tashqaridan qidiradi


def calculate(a): # (2) qiymatni parametrdan qidiradi undaxam bo'lmasa (3) tashqaridan 
    c = a * b    # (1) qiymatni  blockdan qidiradi 
    print(f"the c value: {c}")


calculate(5)


def calculatet(a): # bu xato chunkiy parametrda 1ta yaniy a parametrni berib
    c = a * b    
    print(f"the c value: {c}") 
    
    calculatet(5, 50) #argumentda 2ta argument keltirish xato