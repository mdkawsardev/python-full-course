# List in Python
#? Lists are used to store multiple data in a single variable
#* Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#? Lists are created using square brackets:

my_list = [1, 2, 3, 4, 5] #* a list
print(my_list)
#* To know data type of a list
print(type(my_list))

#? List Items
#! List items are ordered, changeable, and allow duplicate values.
#* List items are indexed, the first item has index [0], the second item has index [1] etc.

#? Lists allow duplicate values:
x = ["imran", "kawsar", "rahul", "imran"]
print(x)

#? length of this list
print(len(x))

#? List items can be of any data type:
#* str, int, bool, float
y = ["hello", 9, True, 9.00]
print(y)

#? list() constructor
z = list((1, 2, 3, 4, 5)) #* note the double round-brackets
print(z)
print(type(z))

