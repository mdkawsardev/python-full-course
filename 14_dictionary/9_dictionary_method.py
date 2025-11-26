# Dictionary Methods
#? Python has a set of built-in methods that you can use on dictionaries.

"""
?Method                                     Description
Clear()                                     Removes all the elements from the dictionary
Copy()                                      Returns a copy of the dictionary
fromkeys()                                  Returns a dictionary with the specified keys and value
get()                                       Returns the value of the specified key
items()                                     Returns a list containing a tuple for each key value pair
keys()                                      Returns a list containing the dictionary's keys
pop()                                       Removes the element with the specified key
popitem()                                   Removes the last inserted key-value pair
setdefault()                                Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()                                    Updates the dictionary with the specified key-value pairs
values()                                    Returns a list of all the values in the dictionary

"""

my_dict1 = {
    "Type": "Human",
    "Name": "Imran",
    "Age": 23,
    "Profession": "Web developer",
    "Married": False
}
print(my_dict1)
#? Copy the dictionary
my_dict2 = my_dict1.copy() #* Copied dictionary

#? Clear the dictionary 'my_dict1'
my_dict1.clear() #* Cleared dictionary

#? fromkeys() method
keys = my_dict2.keys()
value = 0
print(my_dict2.fromkeys(keys, value)) #* The fromkeys() method returns a dictionary with the specified keys and the specified value.

#? get() method
get = my_dict2.get("Type") #* Returns the value with spcified key
print(get)

#? items() method
item = my_dict2.items() #* Returns a list containing a tuple for each key value pair
print(item)

#? keys() method
key = my_dict2.keys() #* Returns all keys in a list
print(key)

#? pop() method
my_dict2.pop("Married") #* Removes an element with specified key
print(my_dict2)

#? popitem() method
my_dict2.popitem() #* Removes the last inserted key-value pair
print(my_dict2)

#? update() method
my_dict2.update({"Profession": "Python Developer"}) #* Updates the dictionary with the specified key-value pairs
print(my_dict2)

#? values() method
value = my_dict2.values() #* Returns all the values in a list
print(value)

#? setdefault() method
#* keyname = Required. The keyname of the item you want to return the value from
"""
value = Optional.
        If the key exist, this parameter has no effect.
        If the key does not exist, this value becomes the key's value
        Default value None
"""
set_de = my_dict2.setdefault("Profession", "Developer") #* The value 'Developer' is optional. If Profession has no value then 'Developer' will be as value. If Profession has a value then 'Developer' is none.
#? The dictionary named 'my_dict2' has a key named Profession and its value is 'Python Developer', so optional parameter will not execute
print(set_de)
print(my_dict2)