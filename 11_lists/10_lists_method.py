# Lists method in Python
#? Python has a set of built-in methods that you can use on lists.

"""
* .append(items)                             Adds elements to the end of the lists
* .clear()                                   Removes all elements from a list
* .copy()                                    Copies a list to assign into another list
* .count(items)                              Counts elements how much appears in a list and returns the number
* .extend(iterable)                          Adds the elements of a list (or any iterable), to the end of the current list
* .index(items)                              Returns the index of the first element with the specified value
* .insert(index, items)                      Inserts an item with the specified position
* .pop()                                     Removes an item from the end of a list
* .pop(index)                                Removes an item with the specified position
* .remove(items)                             Removes an item with the specified value
* .sort()                                    Sorts a list by alphanumaric by default
* .reverse()                                 Reverses a list(oposite of sorting)

"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2]
list1.append(True) #* Adds items to end of the list
print(list1)
list2 = list1.copy() #* Copied list1
print(list2)
list1.clear()
print(list1) #* Now, it's an empty list
print(list2) #* Still it has a value, because I copied list1 and assigned to list2
print(list2.count(2)) #* Returns counts number. I found 3 because 2 has beed used 3times in this list
list3 = ["hello", "world"]
list2.extend(list3) #* Added elements from list3 to list2
print(list2)
print(list2.index("hello")) #* hello's index number is 12. If I used "hello" 2times then I would get the first one's index
list3.insert(0, "welcome") #* I inserted an item with a specified position
print(list3)
list2.pop(10) #* I removed index 10 which value is 2
print(list2)
list2.pop() #* It removed the last item of the list
print(list2)
list2.remove("hello") #* It removed an item with the specified value
print(list2)

list4 = [53, 43, 62, 0, 1, 4, 6, 8, 3]
list4.sort() #* It sorts alphanumerically by default
print(list4)
list4.reverse()
print(list4) #* It reverses sorting(oposite of sorting)
list5 = ["d", "b", "a", "c"]
list5.sort()
print(list5)
list5.reverse()
print(list5)
list5.sort(reverse= True) #! sort(reverse= True) same as reverse()
print(list5)