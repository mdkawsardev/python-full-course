# Python Function Arguments
#? Arguments
"""
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
"""

#? A function with one argument:
def say_hi(name):
    print("Hello"+ " " +name)
say_hi("kawsar")
say_hi("imran")
say_hi("emon")

#? Parameters vs Arguments
#* The terms parameter and argument can be used for the same thing: information that are passed into a function.
"""
From a function's perspective:

A 'parameter' is the variable listed inside the parentheses in the function definition.

An 'argument' is the actual value that is sent to the function when it is called.
"""
def hello(name): #* name is a parameter
    print("hello"+ " " +name)
hello("kawsar") #* kawsar is an argument

#? Number of Arguments
"""
By default, a function must be called with the correct number of arguments.

If your function expects 2 arguments, you must call it with exactly 2 arguments.
"""
#* This function expects 2 arguments, and gets 2 arguments::
def message(fname, lname):
    print(fname+ " " +lname)
message("imran", "kawsar")

#* If you try to call the function with the wrong number of arguments, you will get an error:
# message("imran")

#? Default Parameter Values
#* You can assign default values to parameters. If the function is called without an argument, it uses the default value:
def hi(name= "Friend"):
    print("Hello" + " " + name)
hi("imran khan")
hi("imran hashmi")
hi()

#? Keyword Arguments
#* You can send arguments with the key = value syntax.
def my_func(animal, name):
    print(f"I have a {animal}, named {name}")
my_func(animal= "Cat", name= "Milo") #* This is called keyword arguments
#* This way, with keyword arguments, the order of the arguments does not matter.
my_func(name= "Milo", animal= "Cat")
#! The phrase 'Keyword Arguments' is often shortened to 'kwargs' in Python documentation.

#? Positional Arguments
#* When you call a function with arguments without using keywords, they are called positional arguments.
#* Positional arguments must be in the correct order:
def hobby(animal, name):
    print(f"I have a cute {animal}, named {name}")
hobby("Cat", "Milo")
#* The order matters with positional arguments:
#* Switching the order changes the result:
hobby("Milo", "Cat")

#? Mixing Positional and Keyword Arguments
#* You can mix positional and keyword arguments in a function call.
#* However, positional arguments must come before keyword arguments:
def my_milo(animal, name, age):
    print(f"I have a {age} year old fantastic {animal}, named {name}")
my_milo("Cat", name= "Milo", age= 2)

#? Passing Different Data Types
#* You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
#* The data type will be preserved inside the function:
#* Sending a list as an argument:
def number(lists):
    for list in lists:
        print(list)
myList = ["Apple", "Banana", "Cherry", "Watermelon"]
number(myList)

#* Sending a dictionary as an argument:
def user(dict):
    print(f"Name is: {dict["name"]}")
    print(f"Age is: {dict["age"]}")
myDict = {"name": "Milo", "age": 2}
user(myDict)

#? Functions can return values using the 'return' statement:
def add(x, y):
    return x + y
print(add(4, 6))

#? Returning Different Data Types
#* Functions can return any data type, including lists, tuples, dictionaries, and more.
#* A function that returns a list:
def check_list():
    lists = ["Bottle", "Mobile", "Desktop"]
    return lists
get_list = check_list()
print(get_list[0])
print(get_list[1])
print(get_list[2])

#* A function that returns a tuple:
def check_tuple():
    tuples = ("T-Shirt", "SweatShirt", "Huddy")
    return tuples
get_tuple = check_tuple()
print(get_tuple[0])
print(get_tuple[1])
print(get_tuple[2])
x, y, z = get_tuple
print("x:", x)
print("y:", y)
print("z:", z)
for i in get_tuple:
    print(i)

#? Positional-Only Arguments
"""
You can specify that a function can have ONLY positional arguments.

To specify positional-only arguments, add ', /' after the arguments:
"""
def my_function(name, /):
    print(f"my name is: {name}")
my_function("Kawsar")
# my_function(name = "Kawsar") #* This will give an error

#? Keyword-Only Arguments
#* To specify that a function can have only keyword arguments, add *, before the arguments:
def my_fun(*, name):
    print(f"My special name is: {name}")
my_fun(name= "Kawsar")
# my_fun("Kawsar") #* This will give an error

#? Combining Positional-Only and Keyword-Only
#* You can combine both argument types in the same function.
#* Arguments before / are positional-only, and arguments after * are keyword-only:
def fun(a, b, /, *, x, y):
    print(a + b + x + y)
fun(3, 3, x= 4, y= 4)