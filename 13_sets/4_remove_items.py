# Remove Set Items
#? To remove an item in a set, use the remove(), or the discard() method.
#* Remove "February" by using the remove() method:
set1 = {"January", "February", "March", "April", "May"}
print(set1)
set1.remove("February")
print(set1)
# print(set1.remove("July")) #* It will raise an error
#! Note: If the item to remove does not exist, remove() will raise an error.

#* Remove "April" by using the discard() method:
set1.discard("April")
print(set1)
print(set1.discard("October")) #* It will return 'None'
#! Note: If the item to remove does not exist, discard() will NOT raise an error.

#* You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#* The return value of the pop() method is the removed item.
#* Remove a random item by using the pop() method:

set2 = {"apple", "banana", "cherry", "watermelon"}
print(set2.pop()) #* It returns removed item
print(set2)

#* Clear the set using 'clear()' method
set3 = {"Year", "Month", "Week", "Day"}
set3.clear()
print(set3)

#* Delete set permanently using 'del' keyword
del set3

# print(set3) #* It will raise an error, because set3 is no longer available




