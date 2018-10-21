#from primes import *
import timeit

# timeit, times how long it takes to run things, setup is the importing 
# number=100 is the number of times it will run 
cy = timeit.timeit('example_cy.test(20)', setup = 'import example_cy', number=100)
py = timeit.timeit('example_py.test(20)', setup = 'import example_py', number=100)

print(cy, py)
print('Cython is {}x faster'.format(py/cy))