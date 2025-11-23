# Sort List
#? Sort List Alphanumerically
#* List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
list1 = ["orange", "cheer", "banana", "melon", "watermelon", "apple"]
list1.sort()
print(list1)
list2 = [100, 423, 3, 5, 7, 1, 0, 4]
list2.sort()
print(list2)

#? Sort Descending
#* To sort descending, use the keyword argument reverse = True:
#* Sort the list descending:
list4 = ["January", "February", "March", "April", "May", "Jun", "July", "August", "September", "October", "November", "December", "z"]
list4.sort(reverse= True)
print(list4)
#* Sort the list descending:
list5 = [82, 52, 12, 4, 0, 100, 44]
list5.sort(reverse= True)
print(list5)

#* Case Insensitive Sort
list6 = ["apple", "Apple", "orange", "Orange", "Banana", "banana", "litchi", "Litchi"]
list6.sort()
print(list6)

#? Reverse Order
#* What if you want to reverse the order of a list, regardless of the alphabet?
#* The reverse() method reverses the current sorting order of the elements.
list6.reverse()
print(list6)


