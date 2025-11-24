# Tuple Methods
#? Python has two built-in methods that you can use on tuples.

"""
? count()                       Returns the number of times a specified value occurs in a tuple
? index()                       Searches the tuple for a specified value and returns the position of where it was found
"""

#? Example
tuple1 = ("January", "February", "March", "January", "January", "March")
print(tuple1.count("January"))
print(tuple1.index("March")) #* It returns the first index of the specified value