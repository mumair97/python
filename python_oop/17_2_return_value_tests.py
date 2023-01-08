## to run this code, we need to have test.py file in the folder

## for testing, you need to check for different options.

import test


def square(x):
    '''raise x to the power'''
    return x*x

print('test square function')
test.testEqual(square(3), 9)
test.testEqual(square(-4), 16) 
test.testEqual(square(1.5), 2.25) 
test.testEqual(square(0), 0) 

# change "*" to + and then check
test.testEqual(square(2), 4) 


##

test.testEqual(sorted([1, 7, 4]), [1, 4, 7])
test.testEqual(sorted([1, 7, 4], reverse=True), [7, 4, 1])
test.testEqual(sorted([1, 7, 4], reverse=False), [1, 4, 7])



