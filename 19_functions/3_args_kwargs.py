# Python *args and **kwargs
#? *args and **kwargs
"""
By default, a function must be called with the correct number of arguments.

However, sometimes you may not know how many arguments that will be passed into your function.

? *args and **kwargs allow functions to accept a unknown number of arguments.
"""
#* Arbitrary Arguments - *args
#* If you do not know how many arguments will be passed into your function, add a * before the parameter name.
#* This way, the function will receive a tuple of arguments and can access the items accordingly:
#* Using *args to accept any number of arguments:
def my_func(*param):
    print(F"These are the items: {param}")
    for i in param:
        print(i)
my_func("apple", "banana", "cherry", "watermelon")
#! Arbitrary Arguments are often shortened to *args in Python documentation.
#? What is *args?
#* The *args parameter allows a function to accept any number of positional arguments.
#* Inside the function, args becomes a tuple containing all the passed arguments:
#* Accessing individual arguments from *args:
def my_ff(*param):
    print(f"Type of item is: {type(param)}")
    print(f"1s item is: {param[0]}")
    print(f"second item is: {param[1]}")
    print(f"Third item is: {param[2]}")
    print(f"All items: {param}")
my_ff("Imran", "Kawsar", "Emon")

#? Using *args with Regular Arguments
#* You can combine regular parameters with *args.
#* Regular parameters must come before *args:
def my_funn(greetings, *names):
    for name in names:
        print(greetings, name)
    print(names)
my_funn("Good Morning", "Imran", "Kawsar", "Emon")
#* In this example, "Hello" is assigned to greeting, and the rest are collected in names.

#? Practical Example with *args
#* *args is useful when you want to create flexible functions:
#* A function that calculates the sum of any number of values:
def make_sum(*numbers):
    totall = 0
    for i in numbers:
        totall += i
    return totall
result1 = make_sum(1, 2, 3, 4, 5)
result2 = make_sum(4, 6, 3, 4, 5)
result3 = make_sum(8, 3, 3, 4, 5)
print(result1) #* sum is 15
print(result2) #* sum is 22
print(result3) #* sum is 23

#* Finding the maximum value:
def max_value(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(max_value(2, 5, 8, 3, 9, 55))

#? Arbitrary Keyword Arguments - **kwargs
#* If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
#* This way, the function will receive a dictionary of arguments and can access the items accordingly:
#* Using **kwargs to accept any number of keyword arguments:
def my_function(**params):
    print(params)
    print(type(params))
    for i in params:
        print(f"{i} = {params[i]}")
my_function(person1 = "imran", person2 = "kawsar", person3 = "emon", person4 = "friend")
#* Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentation.

#? What is **kwargs?
#* The **kwargs parameter allows a function to accept any number of keyword arguments.
#* Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

#? Using **kwargs with Regular Arguments
#* You can combine regular parameters with **kwargs.
#* Regular parameters must come before **kwargs:
def my_funnn(username, **params):
    print(type(params))
    print(f"Username is: {username}")
    for i in params:
        print(f"{i} = {params[i]}")
my_funnn("mdkawsardev", age= 23, profession= "Python developer", marital_status= False)

#? Combining *args and **kwargs
#* You can use both *args and **kwargs in the same function.
"""
The order must be:
1 regular parameters
2 *args
3 **kwargs
"""
print("")
def combining(username, *colors, **details):
    print(f"Type of *args = {type(colors)}")
    print(f"Type of **kwargs = {type(details)}")
    print(f"Username is: {username}")
    print(f"Favourite colors: {colors}")
    for d in details:
        print(f"{d} = {details[d]}")
combining("mdkawsardeveloper", "black", "white", "blue", "skyblue", "gray", name="Imran Kawsar", age=23, profession="Python developer")

#? Unpacking Arguments
#* The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
#* Unpacking Lists with *
#* If you have values stored in a list, you can use * to unpack them into individual arguments:
#* Using * to unpack a list into arguments:
def newFun(a, b, c):
    return a+b+c
myList = [1, 2, 3]
result = newFun(*myList) #* Same as: newFun(1, 2, 3)
print(result)

#? Unpacking Dictionaries with **
#* If you have keyword arguments stored in a dictionary, you can use ** to unpack them:
#* Using ** to unpack a dictionary into keyword arguments:
def dicFun(fname, lname):
    print("Hi", fname, lname)
myDict = {'fname': 'imran', 'lname': 'kawsar'}
newResult = dicFun(**myDict)
#! Remember: Use * and ** in function definitions to collect arguments, and use them in function calls to unpack arguments.

