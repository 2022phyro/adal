#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        a = (max(a_dictionary))
        return a
    except TypeError:
        return "None"
