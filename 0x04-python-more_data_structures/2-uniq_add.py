#!/usr/bin/python3

def uniq_add(my_list=[]):

    uniqe = {i for i in my_list}
    list_sum = 0
    for i in uniqe:
        list_sum += i

    return list_sum
