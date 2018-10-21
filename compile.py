from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("primes",  ["primes.pyx"]),
    Extension("example_cy",  ["example_cy.pyx"]),
#   ... all your modules that need be compiled ...
]

setup(
    name = 'My Program Name',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)