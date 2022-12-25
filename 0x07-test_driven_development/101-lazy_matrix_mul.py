import numpy as np
import sys
"""This module also odoes matrix multiplication, but with two lines of code
"""
def lazy_matrix_mul(m_a, m_b):
    """It uses numpy to carry out matrix multiplication

    Args:
        m_a (list): a matrix of integers or floats
        m_b (list): a matrix of integers or floats

    Returns:
        list: the multiplied result
    """
    try:
        result = np.dot(m_a, m_b)
        return result
    except (TypeError, ValueError):
        print("TypeError: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return TypeError