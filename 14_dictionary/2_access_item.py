# Access Dictionary Items
#? Accessing Items
#* You can access the items of a dictionary by referring to its key name, inside square brackets:
my_dict1 = {
    "Brand": "Marcedez",
    "model": "ghost",
    "color": "black",
    "speed": f"{1800}kph"
}
#accessing "Brand", "model", "color", "speed" keys to get their values
print(my_dict1["Brand"])
print(my_dict1["model"])
print(my_dict1["color"])
print(my_dict1["speed"])

#? There is also a method called get() that will give you the same result:
print("") #* to get a space
print(my_dict1.get("Brand"))
print(my_dict1.get("model"))
print(my_dict1.get("color"))
print(my_dict1.get("speed"))

#! If you want to access items using square brackets if item doesn't exist it will raise an error. 
#! If you want to access items using get() method if item doesn't exist it will not raise an error, it will return none
# print(my_dict1["brand"]) #* Raises an error
# print(my_dict1.get("brand")) #* Returns None

#? Get Keys
#* The keys() method will return a list of all the keys in the dictionary.
x = my_dict1.keys()
print(x)
#* Add a new item to the original dictionary, and see that the keys list gets updated as well:
my_dict1["launch"] = 2026
print(x)

#? Get Values
#* The values() method will return a list of all the values in the dictionary.
y = my_dict1.values()
print(y)
#* Make a change in the original dictionary, and see that the values list gets updated as well:
my_dict1["launch"] = 2025
print(y)

#? Get Items
#* The items() method will return each item in a dictionary, as tuples in a list.
#* Get a list of the key:value pairs
items = my_dict1.items()
print(items)
#* adding new items to the dictionary
my_dict1["Countyr"] = "Germary"
print(items)

#? Check if Key Exists
#* To determine if a specified key is present in a dictionary use the in keyword:
#* Check if "model" is present in the dictionary:
if "model" in my_dict1:
    print("Yes! model is present in the dictionary")