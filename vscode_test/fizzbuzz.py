def fizzbuzz(input):
    if(input % 3 == 0 and input % 5 == 0):
        print("FizzBuzz")
    elif(input % 3 == 0):
        print("Fizz")
    elif(input % 5 == 0):
        print("Buzz")
    else:
        print(input)


fizzbuzz(14)
