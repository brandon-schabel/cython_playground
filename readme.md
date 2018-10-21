Initial tutorial https://medium.com/@xpl/protecting-python-sources-using-cython-dcd940bb188e


Sentdex tutorial
example_cy and example_py
https://www.youtube.com/watch?v=mXuEoqK4bEc

compile command 
python compile.py build_ext --inplace


## Generate HTML report on python interaction
The yellow lines in the html file show  Python interaction, yellow = more
command: 
cython -a example_cy.pyx

## Use pyximport instead of recompiling everytime
To use cython just as you would python
check file pyx_import_test.py
in that file we start pyximport, it checks for changes to our cython file
then recompiles automatically if there is any changes