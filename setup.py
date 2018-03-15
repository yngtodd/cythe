#from distutils.core import setup, Extension
from Cython.Build import cythonize

import sys

import numpy as np
from setuptools import find_packages, setup, Extension
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args or '')
        sys.exit(errno)


# see args descriptions at
# https://docs.python.org/3/distutils/apiref.html#distutils.core.Extension
extensions = [
    Extension(
        name='cythe.cython._cext',
        sources=['cythe/cython/_cext.pyx', 'cythe/src/demo.c'],
        include_dirs=['cythe/include/',  np.get_include()],
        extra_compile_args=['--std=c99']
    )
]

setup(
    name='cythe',
    version='0.1dev',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    install_requires=['cython >= 0.23'],
    tests_require=['pytest >= 2.7.3'],
    cmdclass={'test': PyTest}
)



