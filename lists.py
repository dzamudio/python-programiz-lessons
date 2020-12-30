import constants as DZ

my_list = ['p', 'r', 'o', 'b', 'e']
my_second_list = ['s', 'p', 'a', 'c', 'e']

DZ.LINE("print my_list")

print(my_list[0])

nested_list = [my_list,my_second_list]

DZ.LINE("print nested_list")

print(nested_list)

# slicing lists

DZ.LINE("slicing lists [2:5]")

print(my_list[2:5])

DZ.LINE("slice [:]")

print(my_list[:])

DZ.LINE("changing and adding elements to list(s)")

odd = [2, 4, 6, 8] # you want to make these values odd

odd[0] = 1 # change 1st item duh

print(odd)

DZ.LINE("change 2nd to 4th items")

odd[1:4] = [3, 5, 7]

print(odd)

DZ.LINE("Append to odd list")

odd.append(9)

print(odd)

DZ.LINE("extend odd list")

odd.extend([11, 13, 15])

print(odd)

DZ.LINE("concat list using +")

print(odd + [17, 19, 21])

DZ.LINE("repeat list using *")

print(odd * 3)

DZ.LINE("delete one item")

del odd[-1]

print(odd)

DZ.LINE("delete multiple items")

del odd[1:3]

print(odd)

nameLetters = ['D', 'A', 'N', 'I', 'E', 'L']

DZ.LINE(nameLetters)

nameLetters.remove('E')

DZ.LINE(nameLetters)

DZ.LINE(nameLetters.pop(-1))

DZ.LINE(nameLetters)

DZ.LINE("List Comprehension")

pow2 = [2 ** x for x in range(10)]

DZ.LINE(pow2)

DZ.LINE("List membership test") # !!!

clique = ['DZ', 'Greg', 'Dinero', 'Vianey', 'Jesus', 'Ivan', 'Sergio', 'Israel']

DZ.LINE("Chad?")
DZ.LINE('Chad' in clique)
DZ.LINE("Vianey?")
DZ.LINE("Vianey" in clique)

DZ.LINE("---------- EOL ----------")

DZ.LINE("See more: https://www.programiz.com/python-programming/list")

