#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        c = fct(*args)
        return c
    except:
        print("Exception: {}".format(sys.exec_info()[1]), file=ys.stderr)
        return (None)
