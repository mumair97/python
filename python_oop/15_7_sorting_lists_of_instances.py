class Fruit():
    # pass

    # define a Constructor
    def __init__(self, name, price):
        self.name = name 
        self.price = price
        
    def sort_priority(self):
        return self.price # sort by price

L = [
    Fruit('Cherry', 10),
    Fruit('Apple', 5),
    Fruit('Blueberry', 20)
]

for f in sorted(L, key = Fruit.sort_priority): # key takes function as argument
    # if no key, then python doesn't know how to sort, so runtime error
    print(f.name)
    
## also
# for f in sorted(L, key = lambda x: x.sort_priority()): # key takes function as argument
#     # if no key, then python doesn't know how to sort, so runtime error
#     print(f.name)
    


