import cython

import numpy as np
cimport numpy as np


# Setup interface for C code
cdef extern void c_multiply (double* array, double value, int m, int n)


def multiply(np.ndarray[double, ndim=2, mode="c"] input not None, double value):
    """
    Multiply a numpy array element-wise by a value in place. 

    Parameters:
    ----------
    * `array: [np.ndarray, type=np.float64, shape=(2,)
        Array to be multiplied.
 
    * `value`: [int or float]
        Number to multiply eash element in the array by.
    """
    cdef int m, n
    m, n = input.shape[0], input.shape[1]
    c_multiply (&input[0,0], value, m, n)
    return None
