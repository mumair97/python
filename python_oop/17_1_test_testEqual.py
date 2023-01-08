## to run this code, we need to have test.py file in the folder

import test


def square(x):
    '''raise x to the power'''
    return x*x

print('test square function')
test.testEqual(square(10), 100) # if test fails, execution does not stops here.
print(4)

########################################################################

def blanked(word, revealed_letters):
    return word

test.testEqual(blanked('apple', 'a'), 'a____')  
test.testEqual(blanked('apple', 'ap'), 'ap___')
test.testEqual(blanked('hello', ''), '_____')
test.testEqual(blanked('hello', 'elj'), '_ell_')
test.testEqual(blanked('umair', 'uaimr'), 'umair')
