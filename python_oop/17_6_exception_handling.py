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

# items = ['a', 'b']
items = ['a', 'b', 'c']


try: # try to run this block, if error then jump to except
    print('a')
    third = items [2] # if runtime error, breaks the code here and jumps to except
    print('b')
except: # if no error above, this except block never runs at all
    print('something went wrong')
    third = False
print('I want this run')
    