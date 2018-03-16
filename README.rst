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

.. _cythe.c_addition.cextcython.py: https://github.com/yngtodd/cythe/blob/master/cythe/c_addition/cextcython.py 
.. _src.demo.c: https://github.com/yngtodd/cythe/blob/master/src/demo.c 
