CURRENT_YEAR = 2019
class Person:
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born
        
    def getAge(self):
        return CURRENT_YEAR - self.year_born
    
    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())
    
# alice = Person('Alice Smith', 1990)
# print(alice)    

# class Student:
class Student(Person):
    def __init__(self, name, year_born):
        # self.name = name
        # self.year_born = year_born
        Person.__init__(self, name, year_born)
        self.knowledge = 0
    
    def study(self):
        self.knowledge += 1
        
    # def getAge(self):
    #     return CURRENT_YEAR - self.year_born
    
    # def __str__(self):
    #     return '{} ({})'.format(self.name, self.getAge())
    
alice = Student('Alice Smith', 1990) # instance
print(alice)
alice.study()
print(alice.knowledge)

# even though getAge is not directly defined for Student class, we still access it.
print(alice.getAge())    
