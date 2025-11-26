# Remove Dictionary Items
#? Removing Items
#* There are several methods to remove items from a dictionary:

my_dict1 = {
    "Type": "Human",
    "Name": "Imran",
    "Age": 23,
    "Profession": "Web developer",
    "Married": False
}
print(my_dict1)

#? pop()
#* The pop() method removes the item with the specified key name:
my_dict1.pop("Married")
print(my_dict1)

#? popitem()
#* The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
my_dict1.popitem()
print(my_dict1)
my_dict1.popitem()
print(my_dict1)

#? del keyword
#* The del keyword removes the item with the specified key name:
del my_dict1["Type"]
print(my_dict1)

#! The del keyword can also delete the dictionary completely:

del my_dict1

# print(my_dict1) #* It will raise an error, because the dictionary named 'my_dict1' is no longer available

my_dict2 = {
    "Brand": "BMW",
    "Color": "White", 
    "Year": 2026
}
print(my_dict2)
#? Clear the dictionary using clear() method
my_dict2.clear() #* This clears all items from the dictionary
print(my_dict2) #* Now, It's an empty dictionary