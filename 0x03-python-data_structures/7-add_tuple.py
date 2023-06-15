#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    elm1 = 0
    elm2 = 0

    elm1 = 0 if tuple_a[0:1] == () else tuple_a[0]
    elm1 += 0 if tuple_b[0:1] == () else tuple_b[0]
    elm2 = 0 if tuple_a[1:2] == () else tuple_a[1]
    elm2 += 0 if tuple_b[1:2] == () else tuple_b[1]

    return (elm1, elm2)
