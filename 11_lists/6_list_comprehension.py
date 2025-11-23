#List Comprehension
#! A short hand for loop that will print all items in a list:
#? List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#! The Syntax
# [expression for item in iterable if condition == True]

list1 = ["January", "February", "March", "April", "May", "Jun", "July", "August", "September", "October", "November", "December"]
[print(y) for y in list1]   #* Looping Using List Comprehension

#* Now, I will put these values in another list
newList = [] #* This is a blank list
newList = [x for x in list1] #* I added all the items from list1 to newList
print(newList)
list2 = [x.lower() for x in list1 if "a" in x] #* I put here the items that included "a" word in items
print(list2)

# list3 = [x for x in list1 if x != "january" else "another"]
list3 = [x if x.lower() != "january" else "apple" for x in list1]
print(list3)

#? The iterable can be any iterable object, like a list, tuple, set etc.
#* You can use the range() function to create an iterable:
list4 = [x for x in range(10) if x <= 5]
print(list4)