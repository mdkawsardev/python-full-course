# Add Dictionary Items
#? Adding Items
#* Adding an item to the dictionary is done by using a new index key and assigning a value to it:

my_dict1 = {
    "Type": "Human",
    "Name": "Imran",
    "Age": 23
}
print(my_dict1)
#* Now, I will add an item to the dictionary as key-value pair
my_dict1["Profession"] = "Web developer"
print(my_dict1)

#? Update Dictionary
#* The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
#* The argument must be a dictionary, or an iterable object with key:value pairs.

#* Add a marital status 
my_dict1.update({"Married": False})
print(my_dict1)