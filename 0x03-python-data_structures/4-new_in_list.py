#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    new_list = my_list.copy()

    if (idx < 0):
        return (new_list)

    if (new_list[idx: idx+1] == []):
        return(new_list)

    new_list[idx] = element
    return(new_list)
