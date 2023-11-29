#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1*int(number)
    print("{}".format((str(number)[-1])), end="")
    return str(number)[-1]
