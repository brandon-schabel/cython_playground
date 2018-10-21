import pyximport
pyximport.install()

from example_cy import test

test(20)

print(test(20))