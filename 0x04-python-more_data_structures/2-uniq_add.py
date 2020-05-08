#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = my_list[:]
    result = 0
    for i in set(unique):
        result = result + i
    return (result)
