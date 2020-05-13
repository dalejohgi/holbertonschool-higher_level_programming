#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    keys = []
    for key, val in a_dictionary.items():
        if val is value:
            keys.append(key)
    for i in range(len(keys)):
        del a_dictionary[keys[i]]
    return (a_dictionary)
