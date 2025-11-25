# Python frozenset
#? frozenset is an immutable version of a set.
#* Like sets, it contains unique, unordered, unchangeable elements.
#* Unlike sets, elements cannot be added or removed from a frozenset.
#* Everything like a set except add or remove

set1 = {"a", "b", 3, "c", "d"}
set2 = {1, 2, 3, 4, "a"}
print(set2)
fset1 = frozenset(set1) #* Now, we cannot add or remove items
print(fset1)
print(type(fset1))
fset2 = frozenset(set2)
print(fset2)
result1 = fset1.intersection(fset2) #* all duplicates value
result2 = fset1.difference(fset2) #* all values from first set that are not in other set
result3 = fset1.symmetric_difference(fset2) #* all items except duplicates
print(result1)
print(result2)
print(result3)