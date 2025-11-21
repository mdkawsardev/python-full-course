# Add set items in python
#? Once a set is created, you cannot change its items, but you can add new items.
#* To add one item to a set use the add() method.

my_list = ["imran", "kawsar", "emon"]
print(my_list)
my_list.append("jahid") #* This method adds items to the last of the list
my_list[2] = "rocky" #* To change items to the specified index
print(my_list)
my_list[0:2] = ["apple", "banana"] #* To change the value of items within a specific range. "imran" and "kawsar" will be replaced by "apple" and "banana". index 2 is excluded
print(my_list)
my_list[0:2] = ["lemon", "watermalon", "melon"] #* Here my range is 0 to 2 index, but I can replace index 0 or index 1. I have totall two index to replace, but there is three items. Here two items will replace with previous items, and one of this will be added
print(my_list) #! Result = ["lemon", "watermalon", "melon", "rocky", "jahid"]