# Join lists in Python
#? Join Two Lists
#* There are several ways to join, or concatenate, two or more lists in Python.
#! One of the easiest ways are by using the + operator.
list1 = ["january", "fabruary", "march", "april", "may"]
list2 = [1, 2, 3, 4, 5]
combine_two_lists = list1 + list2
print(combine_two_lists)

#! Another way to join two lists is by appending all the items from list2 into list1, one by one:
for i in list2:
    list1.append(i) #* Adds items by end of the lists
print(list1)

#! Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list3 = ["a", "b", "c", "d"]
list4 = [1, 2, 3, 4]
list3.extend(list4)
print(list3)