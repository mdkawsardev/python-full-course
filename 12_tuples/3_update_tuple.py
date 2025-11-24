# Update Tuples
#? Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#* But there are some workarounds.
#* Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#* But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#! Convert the tuple into a list to be able to change it:

tuple1 = ("January", "February", "March", "April", True)
print(tuple1)
tuple2 = list(tuple1) #* Converted as list
print(type(tuple2))
tuple2[-1] = "May" #* Changed item
tuple1 = tuple(tuple2) #* Converted the list back into the tuple
print(tuple1) #* Now, It's a changeale tuple
print(type(tuple1))

#? Add Items
#* Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
#* 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
#* Convert the tuple into a list, add "orange", and convert it back into a tuple:
tuple3 = ("January", "February", "March", "April")
x = list(tuple3)
y = ("May", "Jun", "July", "August", "September", "October", "November", "December")
for i in y:
    x.append(i)
print(x)
tuple3 = tuple(x)
print(tuple3)

#? Remove Items
tuple4 = ("January", "February", "March", "April", "May", True, 1.00)
print(tuple4)
k = list(tuple4)
k.remove(True) #* Removes by value
k.pop(-1) #* Removes by index
tuple4 = tuple(k)
print(tuple4)

#? Delete tuple permanently
del tuple4 #* This tuple has been permanently deleted. This is no longer available
