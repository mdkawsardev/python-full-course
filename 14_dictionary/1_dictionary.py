# Python Dictionaries
#? Dictionaries are used to store data values in key:value pairs.
#* A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#* Dictionaries are written with curly brackets, and have keys and values:

my_dict1 = {
    "Name": "Imran",
    "Age": 23,
    "Profession": "Student"
}
print(my_dict1)
print(type(my_dict1))

#? Dictionary Items
#* Dictionary items are ordered, changeable, and do not allow duplicates.
#* Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#? Accessing items
print(my_dict1["Name"])
print(my_dict1["Age"])
print(my_dict1["Profession"])
print(len(my_dict1)) #* Dictionary lenght

#? Changeable
#* Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

#? Duplicates Not Allowed
#* Dictionaries cannot have two items with the same key:
#* Duplicate values will overwrite existing values:

my_dict2 = {
    "Name": "Kawsar",
    "Age": 22,
    "Profession": "Student", #* It will be overwritten by second item
    "Profession": "Web developer"
}
print(my_dict2)

#? Dictionary Items - Data Types
#* The values in dictionary items can be of any data type:

my_dict3 = {
    "Name": "Imran", #* Str
    "Age": 23, #* Int
    "Marital status": False, #* Boolean
    "Height": 5.8, #* Floating point
    "Relationship": None, #* None type
    "Color": ["White", "Black", "Ash"] #* Set
}
print(my_dict3)

#? The dict() Constructor
#* It is also possible to use the dict() constructor to make a dictionary.

my_dict4 = dict(
    Brand = "Marcedez",
    model = "ghost",
    color = "black",
    speed = f"{1800}kph"
)
print(my_dict4)