# Python Scope
#? Scope
#* A variable is only available from inside the region it is created. This is called scope.

#? Local Scope
#* A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
#* A variable created inside a function is available inside that function:

def my_func():
    x = 33
    print(x)
my_func()

#? Function Inside Function
#* As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
#* The local variable can be accessed from a function within the function:
def my_funn():
    x = 99
    def inner():
        print(x)
    inner()
my_funn()

#? Global Scope
#* A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#* Global variables are available from within any scope, global and local.
#* A variable created outside of a function is global and can be used by anyone:

y = 90

def number():
    print(y)
number()
print(y)

#? Naming Variables
#* If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
#* The function will print the local x, and then the code will print the global x:
z = 111

def trying():
    z = 222
    print(z)
trying()
print(z)

#? Global Keyword
#* If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#* The global keyword makes the variable global.
#* If you use the global keyword, the variable belongs to the global scope:
def global_keyword():
    global k #* It's global variable, now I can use it anywhere
    k = 900
    print(k)
global_keyword()
print(k) #* I printed 'k' variable out side of the function
#* If you use the global keyword, the variable belongs to the global scope:
#* To change the value of a global variable inside a function, refer to the variable by using the global keyword:
a = 000
def change():
    global a #* I made changes a global variable inside of the function
    a = 999
    print(a)
change()
print(a)

import platform
s = platform.system()
print(s)
d = dir(platform)
print(d)