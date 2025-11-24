# Tuples in Python
#?Tuples are used to store multiple items in a single variable.
#* Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#! A tuple is a collection which is ordered and unchangeable.
#* Tuples are written with round brackets.

tuple1 = ("apple", "banana", "orange")
print(tuple1)
print(type(tuple1))

#? Tuple Items
#* Tuple items are ordered, unchangeable, and allow duplicate values.
#* Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

#? A tuple
tuple2 = ("January", "February", "March", "April")
print(len(tuple2)) #* Length of this tuple

#? A tuple with a single value
tuple3 = ("January") #! A wrong proccess to define a tuple with a single value. It will return as a string 
print(type(tuple3)) #! str
tuple4 = ("January",) #* This is a correct way to define a tuple with a single value. Remember that after a value you must add a comma then it will count as a tuple
print(type(tuple4)) #* Now, It's a tuple with a single value

#? Tuple items can be of any data type:
#* String, int and boolean data types:
tuple5 = ("January", 1, True, False, 1.00)
print(tuple5)
for x in tuple5:
    print(x)

for x in range(len(tuple5)): #* With index number
    print(tuple5[x])

#? Tuple constructor
tuple6 = tuple(("January", "February", True, False, 1, 1.00))
print(type(tuple6))
for x in range(len(tuple6)):
    print(tuple6[x])