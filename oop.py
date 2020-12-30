# imports and other shit here.
import constants as DZ

# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")
    
    def whoisThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

class Parrot:
    
    # class attribute
    species = "bird"
    
    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)
    
    def fly(self):
        print("Parrot can fly")
        
    def swim(self):
        print("Parrot cannot swim")
        
# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
DZ.LINE("Blu is a {}".format(blu.__class__.species))
DZ.LINE("{} is a {} years old".format(blu.name, blu.age))
DZ.LINE(blu.sing("'Happy'"))
DZ.LINE(blu.dance())

# ---------------
# Inheritance
# ---------------

# child class
class Penguin(Bird):
    
    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")
        
    def whoisThis(self):
        print("Penguin")
    
    def run(self):
        print("Run faster")
    
    def fly(self):
        print("Penguin cannot fly")
        
    def swim(self):
        print("Penguin can swim")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

# ---------------
# Encapsulation
# ---------------

class Computer:
    
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# ---------------
# Polymorphism
# ---------------

# common interface
def flying_test(bird):
    bird.fly()

# passing the object
flying_test(blu)
flying_test(peggy)

DZ.LINE( "Object-Oriented Programming makes the program easy to understand as well as efficient." )
DZ.LINE( "Since the class is sharable, the code can be reused." )
DZ.LINE( "Data is safe and secure with data abstraction." )
DZ.LINE( "Polymorphism allows the same interface for different objects, so programmers can write efficient code.")

DZ.LINE( "For more information please visit: https://www.programiz.com/python-programming/object-oriented-programming" )