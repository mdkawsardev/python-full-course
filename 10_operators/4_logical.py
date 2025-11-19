# Logical Operators
#? Logical operators are used to combine conditional statements:

"""
? and                   returns True if both statements are True    (2 < 4 and 5 > 3)
? or                    returns True if one statement is True       (4 == 4 or 5 > 2)
? not                   Reverse the result, returns False if the result is true, not(3 < 5 and 3 > 2)
"""

x = 4
y = 6
print(x == y and x > y)
print(x > y or x < y)
print(not(x > y or x < y))