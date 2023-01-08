## syntactic error = forget commas, brackets etc (python doesn't run our codes at all)
## runtime error = index error (try to fetch 3rd element when you only have 2 elements)
## semantic error = if you want to add but get division (you don't get error but not happy with result)

#########################################

# items = ['a', 'b']
# print('this is going to be printed')
# third = items[2]
# print('this is not going to be reached')

###########################
## try-except

items = ['a', 'b']
# items = ['a', 'b', 'c']


try: 
    myvar = a  # name error
    third = items [2]  # index error
    x = 10/ 0  # zero division error
    print('a')
    # third = items [2]
    
except ZeroDivisionError:
    print('You cannot divide by zero')
except IndexError: 
    print('Index out of bound')
except NameError:
    print('Tried to fetch a name that did not exist')
    
print('this does run')
    