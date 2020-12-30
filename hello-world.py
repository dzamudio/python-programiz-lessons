import constants as DZ
import uuid
import turtle

elsa = turtle.Turtle()
elsa.speed(0)
elsa.hideturtle()
startAngle = 0
hundredths = 0
shift = 0
rangeCounter = 1
for i in range(1000):
    #break
    if startAngle <= 350:
        startAngle += 10
        print(startAngle, uuid.uuid1())
    if startAngle == 360:
        startAngle = 0
        print(startAngle,"---Completed a Revolution");
        # after one complete revolution, shift the circle to the right a bit? yes. a bit.
        shift += 10
        elsa.forward(17)
        elsa.right(5)
    print("cycle:",rangeCounter);
    rangeCounter += 1
    hundredths += 10
    elsa.forward(15)
    elsa.right(10)

print("<html><head><title>Python 1.0</title><style type='text/css'></style></head><body><h1>Hello world.</h1></body></html>")

for i in range(1,11):
    print(i)
    if i == 5:
        break

boolVar1 = True;

# this is a comment line ok.
""" this is a multi line comment
    but it's using three quotes ok """

if boolVar1: print('single line hello'); a = 'SL'; print(a)

if boolVar1:
    print('multi-line hello');
    a = 'ML'
    print(a);
    
def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)

print()
a, b, c = 5, 4.2, "hello"

print (a)
print (b)
print (c)

print()
x = y = z = "same"

print (x)
print (y)
print (z)

print()
print("The value of",DZ.CONST_NAME,"is",DZ.CONST_VAL);

a = 0b10101; #binary Literal
b = 100 #decimal Literal
c = 0o310 #octal Literal
d = 0x12c #hexadecimal Literal

#float Literals
float_1 = 10.5
float_2 = 1.5e2

#complex Literal
x = 3.14j

print("Literal types: binary, decimal, octa, hexadecimal")
print(a, b, c, d)
print("Literal floats")
print(float_1, float_2)
print("complex Literals")
print(x, x.imag, x.real)

print()
print("complex subtraction should be a real 0 number")
print( complex(1,1)-complex(1,1) )

print()
print("complex multiplication should be -1")
print( complex(0,1)*-1 )

print()
print("complex of -1 should be ?")
print( (complex(0,1)*-1).real == 0.0 )

print()

complex1 = 2+2j
print("complex1:")
print(complex1+complex(1,2))

print()
complex2 = -1+-1j
print("complex2:")
print(complex2+complex(0,1))

print()
strings = "Python string of text"
char = "C"
multiline_str = """This is a multi-line string
with more than one line in the code"""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

print()

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

print()

drink = "Available"
food = None #field has not been created

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)
        
menu(drink)
menu(food)

print()

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i', 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
print("length of fruits is",len(fruits))
i = 0
while i < len(fruits):
    i = i+1
    print(i)

print()

print(fruits, "is of type:", type(fruits))
print(complex2, "is complex number?", isinstance(complex2,complex))

print()
longFloat = 0.1234567890123456789123456789 #0.1234567890123456[7]>89123456789
print("longFloat:",longFloat)

print()

a = [5,10,15,20,25,30,35]
print(a[2])
print(a[0:2])

print()
print("id of a is:",id(a))

print()
for i in range(1,100,10):
    print(i, end =" ")
print()

userId = uuid.uuid1()
user = {'id':userId.fields, 'uuid':uuid.uuid4()}
print(user)

print()
a = 5
print(type(a))
print(type(5.0))

c = 5 + 3j
print(c + 3)

print(isinstance(c, complex))

"""
Binary: 0b or 0B
Octal: 0o or 0O
Hexadecimal: 0x 0X
"""

print()
print(0b1101011)
print(0xFB + 0b10)
print(0o15)

stringOverManyLines = ('This is a string that has been '
                       'split over many lines for some '
                       'reason. ')
print(stringOverManyLines)

DZ.LINE("String Membership Test")
if 'noun' in 'adj noun int adj mod noun mod':
    DZ.LINE("N DETECTED")


str = 'Daniel Zamudio'
DZ.LINE(str, "enumerate()")
list_enumerate = list(enumerate(str))
print('list(enumerate(danielzamudio) = ', list_enumerate)
DZ.LINE('len(danielzamudio) = ', len(str))

DZ.LINE("Sets, can be used to store data and can be quickly manipulated like joins!")

tableA = {1, 2, 3, 4, 5}
tableB = {6, 7, 8, 9, 10}

DZ.LINE("OUTER JOIN tableA | tableB")
DZ.LINE(tableA | tableB)

tableA = {1, 2, 3}
tableB = {4, 2, 5}
print(tableA, tableB)

DZ.LINE("LEFT JOIN tableA.union(tableB)")
tableA.union(tableB)
DZ.LINE(tableA)

tableA = {1, 2, 3}
tableB = {4, 2, 5}
print(tableA, tableB)

DZ.LINE("LEFT JOIN tableB.union(tableA)")
tableB.union(tableA)
DZ.LINE(tableB)

tableA = {1, 2, 3}
tableB = {4, 2, 5}
print(tableA, tableB)

DZ.LINE("INNER JOIN tableA & tableB")
print(tableA & tableB)

DZ.LINE("See https://www.programiz.com/python-programming/set for more ways of using and manipulating sets")

dictInformal = {'61c6d95b-00fa-4bf1-84c9-9b822c779abf':'daniel.zamudio@ymail.com', '1de5c31d-dc65-4aee-ad94-173a832f6d25': 'mazamudio@ymail.com'}

dictImplicit = dict({'61c6d95b-00fa-4bf1-84c9-9b822c779abf':'daniel.zamudio@ymail.com', '1de5c31d-dc65-4aee-ad94-173a832f6d25': 'mazamudio@ymail.com'})

DZ.LINE(dictInformal);

DZ.LINE(dictImplicit);

DZ.LINE("dictInformal['61c6d95b-00fa-4bf1-84c9-9b822c779abf'] =", dictInformal['61c6d95b-00fa-4bf1-84c9-9b822c779abf'])

DZ.LINE("dictImplicit.get('61c6d95b-00fa-4bf1-84c9-9b822c779abf') =", dictImplicit.get('61c6d95b-00fa-4bf1-84c9-9b822c779abf'));

DZ.LINE("For more information about dictionaries and methods see: https://www.programiz.com/python-programming/dictionary");