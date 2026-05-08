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
