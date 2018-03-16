.. raw:: html

    <embed>
        <p align="center">
            <img width="300" src="https://github.com/yngtodd/cythe/blob/master/img/deathscythe_space.gif">
        </p>
    </embed>

------------

CYTHE
-----

Compiling a library with Cython extensions. Straight to the point.

Cython is great for two reasons. One, you can wrap existing C code in Python so that it can be called from 
your python libraries. Two, Cython is its own language. It has the feel of Python and runs close to the speed
of C. 

Wrapping C
----------

An example of a python function wrapping a C function can be found in :code:`cythe.c_addition.cextcython.py`:

.. code-block:: python 

    def scalar_int_add(x, y):
    """
    Add two integers.
    """
    return _cext.scalar_int_add(x, y)

:code:`scalar_int_add()` wraps a C function by the same name found in :code:`src.demo.c`:

.. code-block:: c
    
    int scalar_int_add(int a, int b) {
        int c;
        c = a + b;
        return c;
    }

Writing Cython
--------------
