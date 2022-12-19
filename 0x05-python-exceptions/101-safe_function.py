#!/usr/bin/python3
import sysi


def safe_function(fct, *args):
    try:
        c = fct(*args)
        return c
    except:
        print("Exception: {}".format(sys.exec_info()[1]), file=sys.stderr)
        return (None)
