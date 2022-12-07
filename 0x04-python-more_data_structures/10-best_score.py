#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        if type(a_dictionary) != 'dict':
            return "None"
        a = (max(a_dictionary))
        return a
    except TypeError:
        return "None"
