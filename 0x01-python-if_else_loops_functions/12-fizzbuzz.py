#!/usr/bin/python3
def fizzbuzz():
    "Change the multiples of three, and five for fizz buzz"
    for i in range(1, 101):
        if ((i % 3) == 0 and (i % 5 == 0)):
            print("FizzBuzz ")
            continue
        elif ((i % 3) == 0):
            print("Fizz ", end='')
            continue
        elif ((i % 5) == 0):
            print("Buzz ", end='')
            continue
        else:
            print("{} ".format(i), end='')
