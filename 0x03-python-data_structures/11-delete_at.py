#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) is 0:
        return
    elif idx > len(my_list) - 1 or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
