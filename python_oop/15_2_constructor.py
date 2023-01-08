class Point():
    # pass

    # define a Constructor
    def __init__(self, x, y):
        self.x = x # point1.x = 5
        self.y = y # point1.y = 10
        
    
    # define a Method (Its like a function but it belongs to a class)
    def getX(self): # methods always a 1 argument called self unlike functions.
        return self.x  # self.x = point1.x

# creating 2 instances/objects of Point class
# point1 = Point() # error if no arguments given
# point2 = Point()

point1 = Point(5, 10) 
point2 = Point(1, 2)

# print(point1) # Point object
# print(point2) # Point object
# print(point1 == point2) # false becoz both are diff instances 

# instance variable: variable that lives in the instance

# point1.x = 5
# point2.x = 10

# print(point1.x)
# print(point2.x)

print(point1.getX())
print(point2.getX())


