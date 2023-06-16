#!/usr/bin/python3

def uniq_add(my_list=[]):

    uniqe = {i for i in my_list}
    return reduce(lambda a, b: a+b, uniqe)
