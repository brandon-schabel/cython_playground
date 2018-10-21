# frunction with cython typing information
# cpdef int, allows you to set a return type, in  this case an integer
cpdef int test(int x):
  # below setting variables with typing information
  cdef int y = 0
  cdef int i
  for i in range(x):
    y += 1
  return y

def test2(x):
  y = 0
  for i in range(x):
    y += 1
  return y