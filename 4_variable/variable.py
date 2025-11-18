# The definition of a variable
# ? A variable contains storing data

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

? Camel-Case = myVariable, First charachter of a word is lower and second is upper
? Snack-Case = my_variable, using underscore between two words or more
? Pascal-Case = MyVariable, Every first charachter of a word is uppercase
"""

x = 12 # ? assigning values to the variable
y = "Hello World" # ? assigning values to the variable
z = True # ? assigning values to the variable
k = 232.232 # ? assigning values to the variable
print(x, y, z, k)
a, b, c = "name", True, 1212
print(a)
print(b)
print(c)
# ? Output the variable's data

# ? Casting of variables
# A data type can be changed with another data type using casting. Example bellow
my_string = "1212" # ? This is a string type data
my_number = 1212 # ? This is an int(integer) type data
my_bool = True # ? This is a boolean type data
my_float = 1.00 # ? This is a floating point data
# To know their's data type, I will use type() method
print(type(my_string))
print(type(my_number))
print(type(my_bool))
print(type(my_float))
# Now I will change each item's data type using casting
cast1 = int(my_string) # ? Now it's a int type data
cast2 = str(my_number) # ? Now it's a string type data
cast3 = float(my_bool) # ? Now it's a floating point data
cast4 = bool(my_float) # ? Now it's a boolean type data

t = "Hello World"
#? c = int(t)  It will raise an error, because letter cannot be an integer


# Global or Local variable

# ? A variable is normally global, it can be used anywhere
g = 12
# I'm calling this variable inside of the function
def myfunc():
    print(g)
myfunc()

# Now, I will create a variable outside of the function and inside of the function
f = 15
def func():
    f = 20 # ? It's a local variable, It will never change the previous variable's value
    print(f)
print(f) # ? Output is 15
func() # ? Output is 20

# Now, I will change the value of outside variable
m = 25 
def fnc():
    global m # ? I used global keyword, because I'm changing the global variable inside of the function
    m = 40
fnc()
print("The value is:",  m) # ? Output is now 40