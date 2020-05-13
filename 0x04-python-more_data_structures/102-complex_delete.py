def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    keys =[]
    for key, val in a_dictionary.items():
        if val is value:
            keys.append(key)
    if keys:
        del a_dictionary[key]
    return ()