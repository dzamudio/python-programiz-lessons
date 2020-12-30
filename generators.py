import constants as Site
DZ = Site.Core()
DZ.line("DZ module initiated")
#import inspect
import pprint
#########################DZ.line("HEADER ##########################

DZ.line("Generators takes the work out of building custom iterators*")
DZ.line("Using yield instead of return in a normal function")
DZ.line("return terminates the function entirely, whereas yield pauses it saving it's state")
DZ.line("local variables and their states are remembered between successive calls.")

# A simple generator function
def my_gen():
    n = 1
    print('THis is printed first')
    # Generator function contains yield statements
    yield n
    
    n += 1
    print('This is printed second')
    yield n
    
    n += 1
    print('This is printed at last')
    yield n
    

DZ.line("It returns an object but does not start execution.")
a = my_gen()

DZ.line("Iterate through the items using next()")
next(a)

DZ.line("once the function yields the generator is paused...")
next(a)
next(a)

DZ.line("When the function terminates/finishes StopIteration is raised automatically")
#next(a)

DZ.line("You can use a for loop to work through a generator")
DZ.line("It automatically handles the StopIteration exception internally")
for item in my_gen():
    print(item)

DZ.line("Normally generators are implemented using a loop having a suitable terminating function.")
# reverses a string
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]
    
DZ.line("For loop to reverse the string (or any iterable)")
for char in rev_str("Hello"):
    print(char)
    
DZ.line("You can use generators created anonymously like lambda functions on the fly...")
my_list = [1, 3, 6, 10]
# square each term using list comprehension...
list_ = [x**2 for x in my_list]
# same thing can be done in a generator expression
# generator expressions are surrounded by paranthesis ( )
generator = (x**2 for x in my_list)
DZ.line(list_)
DZ.line("Generator created, it returns an object only...")
DZ.line(generator)
DZ.line("Generators work only On Demand")
a = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

DZ.line("Furthermore, generators can be used as function arguments...")
print( sum(x**2 for x in my_list) )
print( max(x**2 for x in my_list) )

# Comparing two implementations, one standard iterator and
# one generator performing the same function

# complex and big
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n += 1
        return result

# simple, easy, and readable
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

DZ.line("Iterators have to return a sequence and will create the entire sequence in memory")
DZ.line("Generators are memory efficient! it only produces one item at a time. :)")
DZ.line("Generators are great for infinite streams of data :)")
DZ.line("You can pipeline generators too which makes it all super efficient...")

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print( sum( square( fibonacci_numbers(10) ) ) )