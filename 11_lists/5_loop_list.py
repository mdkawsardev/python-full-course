# Loop Through a List
#? You can loop through the list items by using a for loop:
#* You can also loop through the list items by referring to their index number.

list1 = ["January", "February", "March", "April", "May", "Jun", "July", "August", "September", "October", "November", "December"]
for i in range(len(list1)):
    print(list1[i]) #* Looping by their index number

#* Looping by items
for x in list1:
    print(x)
print("")
#? You can also use while loop
k = 0
while k < len(list1):
    print(list1[k]) #* Printing by index number
    k +=1

print("")

