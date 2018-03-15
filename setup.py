#from distutils.core import setup, Extension
from Cython.Build import cythonize

import sys

import numpy as np
from setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommand


setup(
    ext_modules=cythonize("cythe.cython.primes.pyx"),
)

# see args descriptions at
# https://docs.python.org/3/distutils/apiref.html#distutils.core.Extension
extensions = [
    Extension(
        name='cythe.cython._cext',
        sources=['cext23/cython/_cext.pyx', 'src/demo.c'],
        include_dirs=['src/', np.get_include()],
        extra_compile_args=['--std=c99'])
]

setup(
    name='cext23',
    version='0.1dev',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    setup_requires=['cffi >= 1.1'],
    cffi_modules=['cext23/cffi/cextcffi_build.py:ffi'],
    install_requires=['cffi >= 1.1', 'cython >= 0.23'],
    tests_require=['pytest >= 2.7.3'],
cmdclass={'test': PyTest})



