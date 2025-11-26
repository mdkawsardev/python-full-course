# Copy Dictionaries
#? Copy a Dictionary
#! You cannot copy a dictionary simply by typing 'dict2 = dict1', because: 'dict2' will only be a reference to 'dict1', and changes made in 'dict1' will automatically also be made in 'dict2'.
#* There are ways to make a copy, one way is to use the built-in Dictionary method copy().

my_dict1 = {
    "Type": "Human",
    "Name": "Imran",
    "Age": 23,
    "Profession": "Web developer",
    "Married": False
}
print(my_dict1) #* I printed my_dict1
my_dict2 = my_dict1.copy() #* I copied my_dict1 to my_dict2
my_dict1.clear() #* Now, I cleared my_dict1
print(my_dict1) #* Now, It will return en empty dictionary, like this {}
print(my_dict2) #* It will print the dictionary with all items, because I already copied before 'my_dict1' is cleared

#? Another way to make a copy is to use the built-in function dict().
#* Make a copy of a dictionary with the dict() function:

my_dict2 = {
    "Brand": "BMW",
    "Color": "White", 
    "Year": 2026
}
print(my_dict2)
my_dict3 = dict(my_dict2)
del my_dict2 #* I permanently deleted 'my_dict2'
print(my_dict3) #* It will print the copied dictionary
# print(my_dict2) #* It will raise an error, because 'my_dict2' is no longer available
