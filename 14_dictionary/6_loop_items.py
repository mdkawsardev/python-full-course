# Loop Dictionaries
#? Loop Through a Dictionary
#* You can loop through a dictionary by using a for loop.
#* When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#* Print all key names in the dictionary, one by one:
my_dict1 = {
    "Type": "Human",
    "Name": "Imran",
    "Age": 23,
    "Profession": "Web developer",
    "Married": False
}
for x in my_dict1:
    print(x)

#* Print all values in the dictionary, one by one:
for i in my_dict1:
    print(my_dict1[i])

#* Now, I will print all keys:values as pair
for a in my_dict1:
    print(f"{a} = {my_dict1[a]}") #* Now, It will be printed key:value pair

#? You can use the keys() method to return the keys of a dictionary:
for k in my_dict1.keys():
    print(k)

#? You can also use the values() method to return values of a dictionary:
for b in my_dict1.values():
    print(b)


print("")
print(my_dict1.keys()) #* It will return all keys in a list
print(my_dict1.values()) #* It will return all values in a list

#? Loop through both keys and values, by using the items() method:
for x, y in my_dict1.items():
    print(x, y)