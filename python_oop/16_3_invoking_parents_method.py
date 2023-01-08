from random import randrange

# here is the original Pet class
class Pet(): ## Super class
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:] # copy the class attribite, so that when we make changes to it,
        # we won't affect the 
        
    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1
        
    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else: 
            return "bored"


    def __str__(self):
        state = " I'm " + self.name + ". "
        state = " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" %(self.hunger, self.boredom, self.sounds)
        
    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()
        
    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()
        
    def feed(self):
        self.reduce_hunger()
        
    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)
        
    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
        

class Dog(Pet):
    sounds = ['Woof', 'Ruff']
    
    def feed(self):
        Pet.feed(self) # since I haven't specified which Pet instance I am calling feed on, 
        ## then I need to pass in the particular instance as the first argument to Pet.feed
        ## Pet.feed To invoke parent class's feed() method ## here we should have argument self
        ## otherwise parent class's feed() method will never be called 
        print("Arf! Thanks")
        # self.feed() will call the Dog's feed(self) method.
        
d1 = Dog("Astro")
d1.feed() # no self argument becoz d1 is instance 

## the same also works for constructors, for example

class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs. 
        self.chirp_number = chirp_number # now, also assign the new instance variable
        
    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()
        
b1 = Bird('twweety', 5)
b1.teach("Polly wanna cracker")
b1.hi()

## choose the answer
print(b1.sounds) # output is ["chirp"]

## for the Dog class defined, if the Pet.feed(self) line is deleted/commented?
print(d1.feed()) # The string would print but d1 won't have its hunger reduced.

        
        
        