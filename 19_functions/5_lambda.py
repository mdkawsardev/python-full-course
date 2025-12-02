# Lambda function in Python
#? Lambda Functions
#* A lambda function is a small anonymous function.
#* A lambda function can take any number of arguments, but can only have one expression.

#? Syntax
#* lambda arguments : expression
#* The expression is executed and the result is returned:
#* Add 10 to argument a, and return the result:
x = lambda a: a + 20
print(x(20))
#* Lambda functions can take any number of arguments:

#* Multiply argument a with argument b and return the result:
y = lambda a, b: a * b
print(y(3, 5))

#* Summarize argument a, b, and c and return the result:
z = lambda a, b, c: a + b + c
print(z(2, 3, 4))

#? Why Use Lambda Functions?
#* The power of lambda is better shown when you use them as an anonymous function inside another function.
#* Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
    return lambda a: a * n
result = myfunc(4)
result2 = myfunc(3)
print(result(11))
print(result2(11))