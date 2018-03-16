.. raw:: html

    <embed>
        <p align="center">
            <img width="300" src="https://github.com/yngtodd/cythe/blob/master/img/deathscythe_space.gif">
        </p>
    </embed>

------------

CYTHE
-----

A simple example showing how to add Cython and C to your Python libraries.

Cython is great for two reasons. One, you can wrap existing C code in Python so that it can be called from 
your python libraries. Two, Cython is its own language. It has the feel of Python and runs close to the speed
of C. 

Wrapping C
----------

An example of a python function wrapping a C function can be found in cythe.c_addition.cextcython.py_:

.. code-block:: python 

    def scalar_int_add(x, y):
    """
    Add two integers.
    """
    return _cext.scalar_int_add(x, y)

:code:`scalar_int_add()` wraps a C function by the same name found in src.demo.c_:

.. code-block:: c
    
    int scalar_int_add(int a, int b) {
        int c;
        c = a + b;
        return c;
    }

Writing Cython
--------------

Cython code is very similar to Python, but where we statically type our variables. A Cython example can be found in primes.pyx_:

.. code-block:: python

    def primes(int kmax):
    """Find the first kmax primes.
    Parameters:
    ----------
    * `kmax`: [int]
        Maximum number of primes to return.
    """
    cdef int n, k, i
    cdef int p[1000]
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result


Calling On the C Standard Library
---------------------------------

When it comes to the standard C library, Cython has already you covered. You can readily :code:`cimport` the
functions you need. Check out the example calling C's :code:`atoi()` in atoi_pyx_:

.. code-block:: python

    from libc.stdlib cimport atoi


    cpdef parse_charptr_to_py_int(char* s):
    assert s is not NULL, "Byte string value is NULL."
    return atoi(s)

Making use of the of Cython's connection to C from Python can be seen in atoi_py_:

.. code-block:: python

   from cythe.c_stdlib import _atoi


    def parse_charptr_to_py_int(s):
        """
        Convert string to int.
    
        Parameters:
        ----------
        * `s`: [str]
            String to be converted to int.
        """
    return _atoi.parse_charptr_to_py_int(s)

.. _cythe.c_addition.cextcython.py: https://github.com/yngtodd/cythe/blob/master/cythe/c_addition/cextcython.py 
.. _src.demo.c: https://github.com/yngtodd/cythe/blob/master/src/demo.c 
.. _primes.pyx: https://github.com/yngtodd/cythe/blob/master/cythe/cython_primes/primes.pyx
.. _atoi.pyx: https://github.com/yngtodd/cythe/blob/master/cythe/c_stdlib/_atoi.pyx
.. _atoi.py: https://github.com/yngtodd/cythe/blob/master/cythe/c_stdlib/atoi.py
