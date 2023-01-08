class Point():
    # pass

    # define a Constructor
    def __init__(self, x, y):
        self.x = x # point1.x = 5
        self.y = y # point1.y = 10
        
    
    # define a Method (Its like a function but it belongs to a class)
    def getX(self): # methods always a 1 argument called self unlike functions.
        return self.x  # self.x = point1.x
    
    def getY(self):
        return self.y
    
    def distanceFromOrigin(self):
        return ((self.x ** 2) +(self.y ** 2)) ** 5
    
    def __str__(self):  # to pring out the string in readable format and not just Point object
        return 'Point ({}, {})'.format(self.x, self.y)
    
    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)
    
    # ## the Python doesn't know how to add two instances p1 + p2 so we  define another Method
    # def __add__(self, otherPoint): # self = p1, otherPoint = p2
    #     return Point(self.x + otherPoint.x,
    #                  self.y + otherPoint.y)
        
    # def __sub__(self, otherPoint): # self = p1, otherPoint = p2
    #     return Point(self.x - otherPoint.x,
    #                 self.y - otherPoint.y)
        
    

p = Point(3, 4) 
q = Point(5,12)

mid  = p.halfway(q) # should return a new Point that is halfway between p and q.
print(mid)

print(mid.getX())
print(mid.getY())



