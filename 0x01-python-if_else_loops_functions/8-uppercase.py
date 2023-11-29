#!/usr/bin/python3
def uppercase(str):
    for i in str:
        up = ord(i)
        if ord(i) >= 97 and ord(i) <= 122:
            up =ord(i) - 32
        print("{}".format(chr(up)), end="")
    print('\n')
