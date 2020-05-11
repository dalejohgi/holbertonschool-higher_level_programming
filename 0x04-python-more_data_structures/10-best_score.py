#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_one = 0
    best_key = ""
    for name, score in a_dictionary.items():
        if score >= best_one:
            best_one = score
            best_key = name
    return (best_key)
