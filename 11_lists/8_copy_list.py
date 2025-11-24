# Copy a List
#? You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#* Use the copy() method
#* You can use the built-in List method copy() to copy a list.

list1 = ["January", "February", "March", "April"]
list2 = list1.copy() #* Copied list1 to list2
print(list2)

#? Another way to make a copy is to use the built-in method list().
list3 = list(list1) #* Copied list1 to list3
print(list3)

#? You can also make a copy of a list by using the : (slice) operator.
list4 = list1[:] #* Copied list1 to list4
print(list4)
print("")
list5 = list1 #* You cannot copy like this because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
print(list5)