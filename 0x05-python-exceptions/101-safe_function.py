#!/usr/bin/python3
def safe_function(fct, *args):
    c = None
    try:
        c = fct(*args)
    except TypeError as err:
        print("Exception: {err}".format(err))
    except ZeroDivisionError as err:
        print("Exception: {err}".format(err))
    except RuntimeError as err:
        print("Exception: {err}".format(err))
    except ValueError as err:
        print("Exception: {err}".format(err))
    except NameError as err:
        print("Exception: {err}".format(err))
    except IndexError as err:
        print("Exception: {}".format(err))
    finally:
        return c