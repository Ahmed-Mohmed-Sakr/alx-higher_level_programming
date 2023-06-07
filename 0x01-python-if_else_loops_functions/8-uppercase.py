#!/usr/bin/python3

def uppercase(str):
    for c in str:
        num = ord(c)
        if ord(c) >= 97 and ord(c) <= 123:
            num -= 32
        print("{}".format(chr(num)), end="")
    print("")
