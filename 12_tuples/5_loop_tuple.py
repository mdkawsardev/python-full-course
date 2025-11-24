# Loop Through a Tuple
#? You can loop through the tuple items by using a for loop.
#* Iterate through the items and print the values:
tuple1 = ("January", "February", "March", "April", "May", "Jun", "July")
for x in tuple1:
    print(x)
#* Print all items by referring to their index number:
for x in range(len(tuple1)):
    print(tuple1[x])

print("")
#* Using a while loop
x = 0
while x < len(tuple1):
    print(tuple1[x])
    x += 1