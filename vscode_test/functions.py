# Basic function with strong types
# :int defines type of arguments
# -> defines return type


def increment(number: int, by: int = 1) -> tuple:
    result = number + by
    print(number, " incremented by ", by, " is ", result)
    return (number, result)


x = 2
y = 3

print("Original X = {}, incremented X = {}"
      .format(*increment(x, y)))  # * unpacks tuples into arguments


# Passing variable number of arguments as a tuple using *
# *args


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print("Total=", multiply(1, 2, 3, 4))

# Passing variable number if arguments as a dictionary using **
# **args


def save_user(**user):
    print(user)
    print(user["name"])
    print(user["id"])


save_user(name="Tejas", id=1)
