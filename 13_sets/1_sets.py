# Sets in Python
#? Sets are used to store multiple items in a single variable.
#* Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#* A set is a collection which is unordered, unchangeable*, and unindexed.
#! * Note: Set items are unchangeable, but you can remove items and add new items.
#* Sets are written with curly brackets.

my_set = {"January", "February", "March", "April"}
print(my_set)
print(type(my_set)) #* To know type
#!Note: Sets are unordered, so you cannot be sure in which order the items will appear.
#* Set items are unordered, unchangeable, and do not allow duplicate values.
#* Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#? Duplicate not allowed
set1 = {"Morning", "Noon", "Night", "Morning"} #* duplicate value will be ignored
print(set1)
#! Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

set2 = {"a", True, "b", 1, False, 0} #* True and 1 are the same value, and False and 0 are the same value. So 1 and 0 will be ignored
print(set2)
print(len(set2)) #* length of this set

#* Set items can be of any data type:
set3 = {"imran", 2, True, 3.00}
print(set3)

#? The set() Constructor
set4 = set(("name", "age", True, 33)) #* note the double round-brackets
print(set4)