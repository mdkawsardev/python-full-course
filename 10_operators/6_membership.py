# Membership Operators
#? Membership operators are used to test if a sequence is presented in an object:

"""
? in                Returns True if a sequence with the specified value is present in the object	x in y
? not in            Returns True if a sequence with the specified value is not present in the object	x not in y
"""

#* Example here...
x = [1, 2, 3, 4] #? a list
print(1 in x) #* Retuns True, because 1 is present in x object
print(0 not in x) #* Returns True, because 0 is not present in x object
print(5 in x) #* Returns False, because 5 is not present in x object

y = ("apple", "banana", "mango") #? a tuple
print("banana" in y) #* Returns True
print("litchi" in y) #* Returns False
print("litchi" not in y) #* Returns True

z = "my name is imran" #? a string
print("m" in z) #* Returns True
print("my" in z) #* Returns True
print("ka" in z) #* Returns False
print("ka" not in z) #* Returns True