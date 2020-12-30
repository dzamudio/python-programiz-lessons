#from config import subConfig1
#print()
#print(config.ABC)
#print()
# See https://www.programiz.com/python-programming/modules for more.
#import config as configuration
#print("config variable a is:", configuration.a)

global CONTINUE
CONTINUE = "Press Enter to Continue"

from decimal import Decimal as D

from config import subConfig1
print()
print(subConfig1.ABC)
print()

print(1.1 + 2.2)
print( D(1.1+2.2) )

input(CONTINUE)

import random

print(random.randrange(10, 20))

input(CONTINUE)

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice

print(random.choice(x))

input(CONTINUE)

# Shuffle x
random.shuffle(x)
print(x)

input(CONTINUE)

print(random.random())

input(CONTINUE)

"""
Packages for directories
Modules for files

A directory must contain a file named __init__.py

Game.Level.start.select_difficulty(2)

from Game.Level import start
>>>start.select_difficulty(2)

from Game.Level.start import select_difficulty
>>> select_difficulty(2)
"""

def factorial(x):
    print(" x =",x)
    if x == 1: # base condition, to avoid stack overflow
        return 1
    else:
        print(x,"* factorial(",x,"-1)")
        return (x * factorial(x-1))
    
num = 3
print("The factorial of", num, "is", factorial(num))
"""
factorial(3)          # 1st call with 3
3 * factorial(2)      # 2nd call with 2
3 * 2 * factorial(1)  # 3rd call with 1
3 * 2 * 1             # return from 3rd call as number=1
3 * 2                 # return from 2nd call
6                     # return from 1st call

see: https://www.programiz.com/python-programming/recursion 
"""
print()
double = lambda x: x * 2
print(double(5))

print()
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list( filter( lambda x: (x%2 == 0), my_list ) )
print(new_list)

new_list = list( map( lambda x: x * 2, my_list ) )
print(new_list)

print()
x = 5
def foo():
    x = 10
    print("local x:", x)
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner x:", x)
    
    inner()
foo()
print("global x:", x)



