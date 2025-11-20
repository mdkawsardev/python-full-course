# Identity Operators
#? Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

"""
? is                Returns True if both variables are the same object	x is y
? is not            Returns True if both variables are not the same object	x is not y
"""
#* Example here...
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = x
print(x is z) #* Returns True, because x and z both have the same object, and in the same memory location
print(x is y) #* Returns False, because x and y both have the same value but not the same object and same memory location
print(x == y) #* Returns True, because x and y both have the same value

print("")
#? I understood this expression
print(x is not z) #* Returns False
print(x is not y) #* Returns True