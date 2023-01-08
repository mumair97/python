class Point():
    # pass
    # define a Method (Its like a function but it belongs to a class)
    def getX(self): # methods always a 1 argument called self unlike functions.
        return self.x  # self.x = point1.x

# creating 2 instances/objects of Point class
point1 = Point()
point2 = Point()

# print(point1) # Point object
# print(point2) # Point object
# print(point1 == point2) # false becoz both are diff instances 

# instance variable: variable that lives in the instance

point1.x = 5
point2.x = 10

# print(point1.x)
# print(point2.x)

print(point1.getX())
print(point2.getX())


