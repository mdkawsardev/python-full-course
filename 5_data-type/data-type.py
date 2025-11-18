# Data type in Python
"""

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType

"""
name = "Imran" # ? This is a string
number = 1212 # ? This is a number
floating = 1.00 # ? This is a float
boolean = True, False # ? This is a boolean
nothing = None # ? This is none type
rangee = range(10) # ? This is a range
comp = 1j # ? This is a complex number
li = ["imran", True, 111, 1.232, False, 1j] # ? This is a list
tup = ("imran", True, 1232, 2.03, False, 1j) # ? This is a tuple
sett = {"imran", True, 4343, 3.00, False, 1j} # ? This is a set
frozen = frozenset({"apple", "banana", "cherry"}) # ? This is a frozenset
dictionary = { # ? This is a dict/dictionary
    "name": "Imran",
    "age": 23,
    "relationship": False,
    "loyalty": True,
    "gpa": 4.33
}
# To know which data type it is, I will use type() method
print(type(name))
print(type(number))
print(type(floating))
print(type(boolean))
print(type(nothing))
print(type(rangee))
print(type(comp))
print(type(li))
print(type(tup))
print(type(sett))
print(type(frozen))
print(type(dictionary))


# Setting the Specific Data Type
x = str("Hello World")	                        #? str	
x = int(20)	                                    #? int	
x = float(20.5)	                                #? float	
x = complex(1j)	                                #? complex	
x = list(("apple", "banana", "cherry"))	        #? list	
x = tuple(("apple", "banana", "cherry"))	    #? tuple	
x = range(6)	                                #? range	
x = dict(name="John", age=36)	                #? dict	
x = set(("apple", "banana", "cherry"))	        #? set	
x = frozenset(("apple", "banana", "cherry"))	#? frozenset	
x = bool(5)	                                    #? bool	
x = bytes(5)	                                #? bytes	
x = bytearray(5)	                            #? bytearray	
x = memoryview(bytes(5))                        #? memoryview
