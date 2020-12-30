import constants as Site
DZ = Site.Core()
DZ.line("DZ module initiated")
#import inspect
import pprint
#########################DZ.line("HEADER ##########################

DZ.line("Iterating through an iterator")

DZ.line("define list")
my_list = [4,7,0,3]
DZ.line("get an iterator using iter()")
my_iter = iter(my_list)
DZ.line("iterate through it using next()")

DZ.line("output: 4")
print(next(my_iter))
DZ.line("output: 7")
print(next(my_iter))

DZ.line("next(obj) is same as obj.__next__()")

DZ.line("Output: 0")
print(my_iter.__next__())

DZ.line("Output: 3")
print(my_iter.__next__())

#DZ.line("This will raise an error, no items left")
#next(my_iter)

# custom iterator #

class PowTwo:
    """Class to implement an iterator
    of powers of two"""
    
    def __init__(self, max=0):
        self.max = max
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
    

DZ.line("create an object")
numbers = PowTwo(3)

DZ.line("create an iterable from the object")
i = iter(numbers)

DZ.line("Using next to get to the next iterator element")
print(next(i))
print(next(i))
print(next(i))

DZ.line("Now for some infinite iterators")
int()
inf = iter(int,1)
next(inf)
next(inf)

class InfIter:
    """Infinite iterator to return all
    odd numbers"""
    
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        num = self.num
        self.num += 2
        return num
    
a = iter(InfIter())
print(next(a))
print(next(a))
print(next(a))
print(next(a))