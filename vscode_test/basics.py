import math

students_count = 1000
rating = 4.99
is_published = True
course_name = """
Multi
line
"""

x, y = 1, 2
x = y = 1

print(type(students_count))
print(id(students_count))


x = [1, 2, 3]
print(x, "@", id(x))
x.append(4)
print(x, "@", id(x))


message = "Python Programming"
print(len(message))
print(message[0])
print(message[-1])
print(message[0:3])
print(message[:3])
print(message[4:])
print(message[2:-1])

first = "Tejas"
last = "Kumar"
full = first + " " + last
print(full)
full = "{} {}".format(first, 2+2)
print(full)
full.upper


PI = -3.14
print(round(PI))
print(abs(PI))

x = input("x: ")

print(int(x))
print(bool(x))
print(float(x))
