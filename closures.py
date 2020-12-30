import constants as Site
DZ = Site.Core()
DZ.line("DZ module initiated")
#import inspect
import pprint
#########################DZ.line("HEADER ##########################

DZ.line("function accessing a non-local variable")

def print_msg(msg):
    # outer enclosing scope
    
    def printer():
        # nested scope func.
        print(msg)
    
    printer()

print_msg("Hello")

# Closure Criteria
print("""
We must have a nested function (function inside a function).
The nested function must refer to a value defined in the enclosing function.
The enclosing function must return the nested function.
""")

# now to demonstrate closure
def print_msg_demo(msg):
    # outer enclosing scope
    
    def printer():
        # nested scope func.
        print(msg)
    
    return printer # returns nested function to close

# now demo...
another = print_msg_demo("Hello Demo")
another()
del print_msg_demo
# try calling it again and whatch what happens...
another()
# the value of another is saved into the variable even though the function is gone...
#print_msg_demo("Hello Demo gone?")

DZ.line("""Use closures in lieu of a class when there .
           is only one method to be implemented. It's more elegant""")

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

DZ.line("Set multiplier of 3")
times3 = make_multiplier_of(3)
print( times3.__closure__ )
DZ.line("Set multiplier of 5")
times5 = make_multiplier_of(5)
print( times5.__closure__ )

print( times3(9) )
print( times5(3) )
print( times5( times3(2) ) )
