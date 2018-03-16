import sys
import numpy as np
from Cython.Build import cythonize
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


extensions = [
    Extension(
        name='cythe.c_addition._cext',
        sources=['cythe/c_addition/_cext.pyx', 'src/demo.c'],
        include_dirs=['include/',  np.get_include()],
        extra_compile_args=['--std=c99']
    ),
    Extension(
        name='cythe.cython_primes.primes',
        sources=['cythe/cython_primes/primes.pyx'],
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



