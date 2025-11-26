# Change Dictionary Items
#? Change Values
#* You can change the value of a specific item by referring to its key name:

#* Creating a new dictionary named my_dict1
my_dict1 = {
    "Brand": "Marcedez",
    "model": "ghost",
    "color": "black",
    "speed": f"{1800}kph"
}
print(my_dict1)

#* Adding new item
my_dict1["year"] = 2025
print(my_dict1)

#* Changing item by reffering key name
my_dict1["year"] = 2026
print(my_dict1)

#? Update Dictionary
#* The update() method will update the dictionary with the items from the given argument.
#* The argument must be a dictionary, or an iterable object with key:value pairs.
#* Update the "model" of the car by using the update() method:
my_dict1.update({"model": "7 series"})
print(my_dict1)


