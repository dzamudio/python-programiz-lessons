import math
import sys
import pprint
import this
import json
from urllib.request import urlopen
with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

print()
input("Press Enter to view import docstrings")
print("*************************************");
print()
print(math.__doc__)
print(sys.__doc__)
print(pprint.__doc__)
print(this.__doc__)
print(json.__doc__)

print()
input("Press Enter to continue")


pp = pprint.PrettyPrinter(indent=4)
print("*************************************");
print("*************************************");
print("*************************************");
pp.pprint(project_info)
print("*************************************");
print("*************************************");
print("*************************************");
print(type(project_info))
print("*************************************");
print("*************************************");
print("*************************************");


#num = int( input("Enter a number: ") )
#print("Your number is: ", num)
#num2 = int( input("Enter a second number: ") )
#print("Total: ", (num + num2) )

print(math.pi)

# syntax can be cleaner here, need to modify Python source for this.
pp.pprint(sys.path)

""" ARITHMETIC OPERATORS

+ add
- subract
* multiply
/ divide (always a float)
% modulus (the remainder of a divide if any)
// floor division (results in a rounded-down whole num.
** Exponent (left operrand raised to the pow(right operand)

    COMPARISON OPERATORS
> greater than
< less than
== equal to
!= not equal to
>= greater than or equal to
<= less than or equal to

    LOGICAL OPERATORS
and (logical) x and y
or (logical) x or y
not (is logical) not x

    BITWISE OPERATORS
& Bitwise AND | x & y = 0 (0000 0000)
| Bitwise OR | x | y = 14 (0000 1110)
~ Bitwise NOT | ~x = -11 (1111 0101)
^ Bitwise XOR | x ^ y = 14 (0000 1110)
>> Bitwise right shift | x >> 2 = 2 (0000 0010)
<< Bitwise left shift | x << 2 = 40 (0010 1000)

    ASSIGNMENT OPERATORS
= | x = 5 || x = 5
+= | x += 5 || x = x + 5
-= | x -= 5 || x = x - 5
*= | x *= 5 || x = x * 5
/= | x /= 5 || x = x / 5
%= | x %= 5 || x = x % 5
//= | x //= 5 || x = x // 5
**= | x **= 5 || x = x ** 5
&= | x &= 5 || x = x & 5
|= | x |= 5 || x = x | 5
^= | x ^= 5 || x = x ^ 5
>>= | x >>= 5 || x = x >> 5
<<= | x <<= 5 || x = x << 5

    SPECIAL OPERATORS
    IDENTITY OPERATORS
is (comparison)
is not (is not comparison)

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

    SPECIAL OPERATORS
    MEMBERSHIP OPERATORS
in (found in) True
not in (not found in) True


"""

def printHello():
    print("Hi")
a = printHello

a()

print( id( printHello() ) )
print( id( a() ) )

# at any given moment there are at least 3 nested scopes...
# Scope of the current function which has local names
# Scope of the module with has global names
# Outermost scope which has built-in names.
# an item can access it's own insides as well as it's immediate outsides.

def outer_function():
    global a
    b = 20
    def inner_function():
        global a
        c = 30
        print("b = ", b)
        print("a = ", a)
        a = 'uh oh'
        print("a = ", a)
    inner_function()

a = 10 # in the global namespace

na = input("Press Enter to Continue")

outer_function()

# CONTROL FLOW STRUCTURES AND ITERATION LOOPING/ETC...

if 3 > 5:
    print("3 is > 5")
elif 3 > 4:
    print("3 is > 4")
elif 3 > 3:
    print("3 is > 3")
elif 3 > 2:
    print("3 is > 2")
else:
    print("no")


# List
numbersSequence = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variables
sum = 0
iterationCount = 0
for val in numbersSequence:
    iterationCount += 1
    sum = sum+val

print("Number of cycles: ", iterationCount)
print("The sum of the numbers sequence is: ", sum)


for i in range(100):
    if int(i+1) != 77:
        print("not this cycle")
        continue
    if int(i+1) == 77:
        print("Breaking")
        break
    print("cycle: ",int(i+1))
else:
    print("finished for in range(100)"); # doesn't run as "else", runs as "then"

input("Press Enter to start function stuff")
    
n = 10
sum = 0
i = 1
while i <= n:
     sum = sum + i
     i = i+1
     
print("* The sum is", sum, "idunno wtf this is *")


# pass, it's not ingored completely. it's a NOP, it's generally used as a placeholder

def idunnoWTF(args):
    pass

# pass is meant for adding something in the body of a loop or function where emtpy would
# normally be unnacceptable

input("Press Enter to show function rules")

def function_name(params):
    """
    DOCSTRING MFs
        - keyword def starts the function header
        - a function name to uniquely identify teh function (see rules)
        - parameters (arguments) through which we pass values to a function. optional
        - a colon: to mark the end of the function header
        - optional documentation string docstring to describe w/ is going on
        - {body}
        - optional return statement to return value
"""
    pass

print(function_name.__doc__)

def absoluteVal(num):
    if num >= 0:
        return num
    else:
        return -num

print()
print(absoluteVal(2))
print(absoluteVal(-4))
print()


# Assigning arguments in functions:
def hiHowAreYou(resp=[]):
    return resp

print( hiHowAreYou([1,'2','3',4,5,'abc']) )
print()

def anotherFunction(*names):
    print(names)
    for name in names:
        print("Hello",name)

anotherFunction("Monica", "Luke", "Steve", "John")



