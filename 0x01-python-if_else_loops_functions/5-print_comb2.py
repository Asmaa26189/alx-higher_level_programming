#!/usr/bin/python3
for x in range(0, 100):
    if x == 99:
        print("{}".format(x), end="")
    elif x < 10:
        x = '0'+str(x)
    if x != 99:
        print("{}, ".format(x), end="")
