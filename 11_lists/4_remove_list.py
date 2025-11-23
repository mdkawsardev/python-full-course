# Remove specified items in python
"""
? remove()          This method removes s specified items from the list
? pop()             This method removes a specified index from the list
? del               This method deletes a specified iterable(list, tuple, sets, dictionary, etc...)
? clear()           This method clears all the items from an iterable(list, tuple, sets, dictionary, etc...)
"""
#! remove()
list1 = ["apple", "mango", "cherry"]
print(list1)
list1.remove("mango") #* Removes by a specified item
print(list1)

#! pop()
list2 = ["imran", "kawsar", "jakir", "rahul", "yusof"]
print(list2)
list2.pop(2) #* Removes by a specified index
list2.pop() #* If I do not want to remove a specified items it will remove the last item 
print(list2)

#! del
list3 = ["january", "february", "march", "april"]
del list3[1] #* It will delete just an item by index
print(list3)
del list3 #* It will completly delete the list 

#print(list3) #* This will give an error, because I deleted list3 by 'del' keyword, so there is no list called list3

#! clear()
list2.clear() #* It will make an empty list
print(list2) #* Result is an empty list, because I cleared all of items from list2 through clear() method
