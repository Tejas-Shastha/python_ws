
glob_msg = "b"
message = "global"


def greet():
    if True:
        global message
        message = "local"
    # message is scoped outside if block. python has no block level scoping


print(message)
greet()
print(message)
