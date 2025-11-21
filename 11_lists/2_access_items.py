# Access list items in python

my_list= [1, 2, 3, 4, 5]
print(my_list[0]) #* Access the first item of the list. First item's index is 0
#? Accessing all items of the list using for loop
for i in my_list:
    print(i)

#* index number  0         1         2        3
second_list = ["apple", "banana", "Cherry", "pears"]
print(second_list[1]) #* Second item
print(second_list[3]) #* Third item
for x in second_list:
    print(x)

#? Slicing lists
third_list = [1, "apple", True, 2, True, "mango", False, 4]
print(third_list[3:6]) #* Returns index 3 to 5. index 3 is included and 6 is excluded. Result = 2, True, mango
print(third_list[2:]) #* Returns index 2 to the end of the list. index 2 is included
print(third_list[2:0]) #* Returns index 2 to the end of the list. Same as above
print(third_list[:5]) #* Returns index 0 to 4 of the list. index 5 is excluded
print(third_list[0:5]) #* Returns index 0 to 4 of the list. Same as above

"""
? Positive index
             0     1       2   3    4      5       6    7
third_lit = [1, "apple", True, 2, True, "mango", False, 4]
! Negative index
            -8    -7      -6   -5  -4      -3     -2   -1
third_lit = [1, "apple", True, 2, True, "mango", False, 4]

"""
print(third_list[-1]) #* Returns last item of the list
print(third_list[:-1]) #* Returns all the items of the list except -1 index of item
print(third_list[0:-1]) #* Returns all the items of the list except -1 index of item. Same as above
print(third_list[-5:-1]) #* Returns -2 item to -5 item. -5 is included and -1 is excluded

print("papaya" not in third_list) #* Returns True
if "apple" in third_list:
    print("Yes! apple is in the list")