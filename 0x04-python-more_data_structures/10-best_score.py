#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        a = (max(a_dictionary))
        if a_dictionary.count(a) > 1:
            return "None"
        return a
    except TypeError:
        return "None"
