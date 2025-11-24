# Access Tuple Items
#? You can access tuple items by referring to the index number, inside square brackets:
tuple1 = ("January", "February", "March", "April", "May", "Jun", "July")
print(tuple1[0]) #* Accessing the first item by index number
print(tuple1[1]) #* Accessing the second item by index number
print(tuple1[2]) #* Accessing the third item by index number
print(tuple1[-1]) #* Accessing items with negative index. It starts from the end of the tuple and returns last item
print(tuple1[-2])
print(tuple1[-3])

#* Accessing items with a range
#! Positive index
print(tuple1[:5]) #* From 0 to 4 index, index 5 is excluded
print(tuple1[0:5]) #* Same as above line of code
print(tuple1[4:]) #* From 4 to end of the tuple 4 is included
print(tuple1[3:6]) #* From 3 to 5 index, index 6 is excluded

#* Accessing items with a range
#! Negative index
print(tuple1[:-1]) #* All items will be printed except last item
print(tuple1[-6:-1]) #* -6 is included and -1 is excluded

#? Printing items through for/while loop
#* For loop
for x in tuple1: #* by items
    print(x)

for x in range(len(tuple1)): #* by index
    print(tuple1[x])

#* While loop
x = 0
while x < len(tuple1):
    print(tuple1[x])
    x += 1

if "April" in tuple1:
    print("Yes! April in the tuple") #* executes this line

if "September" in tuple1:
    print("Yes! September in the tuple")
else:
    print("Not! September is not in the tuple") #* executes this line

if "August" not in tuple1:
    print("Not! August is not in the tuple") #* executes this line