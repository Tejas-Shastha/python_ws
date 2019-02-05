# x = input("Name: ")
x = "Tejas"
if not x:
    print("Empty input")
else:
    print("Name is {}".format(x))

age = 22
if 18 <= age < 65:
    print("Eligible")

# print(age >= 18 ? "Eligible": "Not eligible") # TERNARY OPERATOR
print("Eligible" if age >= 18 else "Not eligible")

# for x in "Python":
#     print(x)

# for x in ['a', 'b', 'c']:
#     print(x)

for x in range(2, 5):
    print(x)

# for-else block. Else executed if all iterations of for loop are not completed
names = ["aTejas", "Kumar", "Shastha"]
for name in names:
    if name.startswith("T"):
        print(name)
        break
else:
    print("Not found")

guess = 0
answer = 5

while guess != answer:
    guess = int(input("Guess: "))
else:
    print("Correct!")
