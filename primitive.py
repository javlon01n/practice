print("==========")
# in JAVA variable is a name storage location, m m nomlanishi
# in PYTHON, variable is named reference!, object

count = 100
count_type = type(count)
print(f"the count: {count} and:{count_type}")

# method   # .nuqta bosilganda uning state va methodlari chiadi
result1 = count.bit_count()
result2 = count.numerator  # state
print(result1, result2)

print("===string===")
# METHODS: upper() .lower() .title() .find() .replace()


course = "AI Python fulStack"
result = type(course)
print(f"the result (1): {result}")

result = course.title()
print(f"the result (2): {result}")

#course.  # shu xolatda foyda li methodlarni ro'yxatini ko'rish mumkun

result = course.upper()
print(f"the result (3): {result}")

result = course.lower()
print(f"the result (4): {result}")

result = course.replace("fulStack", "MasterClass")
print(f"the result (5): {result}")



print("============")