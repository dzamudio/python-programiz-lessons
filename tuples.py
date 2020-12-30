import constants as DZ

DZ.LINE("Tuples are immutable-cannot be changed.")

DZ.LINE("empty tuple")
my_tuple = ()
print(my_tuple)

DZ.LINE("tuple containing integers")
my_tuple = (1, 2, 3)
print(my_tuple)

DZ.LINE("tuple with mixed datatypes")
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

DZ.LINE("nested tuple")
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

DZ.LINE("tuples can be created without parentheses, known as tuple packing")
my_tuple = 3, 4.6, "dog"

DZ.LINE("tuple unpacked")
a, b, c = my_tuple
print(a,b,c)

DZ.LINE("tuples with only one element need a trailing coma")
my_tuple = ("hello",)
print(type(my_tuple))

DZ.LINE("Show size of tuple and display the last element")
my_tuple = ("A", "B", "C", "D", "E", "F", "G")
print("Tuple size:",len(my_tuple),"Last item:",my_tuple[len(my_tuple)-1])

DZ.LINE("Slicing tuples")
my_tuple = (1, 2, 3, 4, 5)
print("Tuple slice[0:0]",my_tuple[0:3]) # (1, 2, 3)

DZ.LINE("Tuples are immutable-cannot be changed.")
DZ.LINE("HOWEVER- if it contains a list within, that list can be changed")
my_tuple = ("FirstElement", ['item1','item2'])
print(my_tuple)
my_tuple[1][1] = "LOL"
print(my_tuple)

DZ.LINE("You can concat + and multiply * tuples the same way you would with lists")

DZ.LINE("""
Use tuples for mixed content, but use lists for same/similar data types.
Iterating through tuples is faster because tuples are immutable, slight performance boost.
Tuples can contain immutable elements that can be used as a key for a dictionary, with lists this is not possible.
If you have data that doesn't change, implementing as a tuple will guarantee that it remains write-protected.

""")