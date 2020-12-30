import constants as Site
DZ = Site.Core()
DZ.line("DZ module initiated")
#import inspect
import pprint
#########################DZ.line("HEADER ##########################

DZ.line("A decorator takes in a function adds functionality.")
DZ.line("also known as metaprogramming...")

def first(msg):
    print(msg)
    
first("Hello1")

second = first
second("Hello2")

# pass functions to functions as arguments

def inc(x):
    return x+1

def dec(x):
    return x-1

def operate(func, x):
    result = func(x)
    return result

first( operate(inc, 3) )
first( operate(dec, 3) )

# futhermrore a function can return another function

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()
# outputs hello
new()

DZ.line("Decorators then...")

def make_pretty(func):
    def inner():
        print("Decorated")
        func()
    return inner

def ordinary():
    print("Ordinary")

DZ.line(">>> ordinary()")
ordinary()
DZ.line("Decorate ordinary()")
DZ.line("---")
DZ.line(">>> make_pretty(ordinary)")
decorated = make_pretty(ordinary)
decorated()
DZ.line("Generally you decorate a function and reassign it as,")
ordinary = make_pretty(ordinary)

DZ.line("Python offers a syntax to achieve this...")
@make_pretty
def ordinary():
    print("I am ordinary")
# equivalent to...
eq = """
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
"""
print(eq)

# now for attributes in decorators
def smart_divide(func):
    def inner(a, b):
        print("I am going to attempt to divide", a, "and", b)
        if b == 0:
            print("Cannot divide by 0 in this universe")
            return
        
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2, 5)
divide(2, 0)

DZ.line("How to accept any number of arguments")
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

DZ.line("Chaining decorators...")
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
eq = """
def printer(msg):
    print(msg)
printer = star(percent(printer))
"""

printer("Hello")

DZ.line("For more info: https://www.programiz.com/python-programming/decorator")