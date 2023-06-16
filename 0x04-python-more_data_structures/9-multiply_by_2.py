#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    return dict(map(lambda a,b: (a, b ** 2), a_dictionary))
