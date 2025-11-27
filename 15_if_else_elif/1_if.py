# Python If Statement
#? Python Conditions and If statements
#* Python supports the usual logical conditions from mathematics:
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

"""
#* These conditions can be used in several ways, most commonly in "if statements" and loops.
#* An "if statement" is written by using the 'if' keyword.

a = 39
b = 44
if a > b: #* Condition is False
    #* if condition is True this statement will be executed
    #* if condition is False python skips this statement
    print("A is greater then B") #* Python will skip this statement, because condition is False
if a < b: #* Condition is True
    print("A less than B") #* It will be executed

#? How If Statements Work
#* The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.

#? Checking if a number is positive:
number = 22
if number > 0:
    print("Number is positive")

#? Multiple Statements in If Block
#* You can have multiple statements inside an if block. All statements must be indented at the same level.
#* Multiple statements in an if block:
age = 20
if age >= 18:
    print("You're an adult")
    print("You're eligible to drive")

#? Using Variables in Conditions
#* Boolean variables can be used directly in if statements without comparison operators.
is_logged_in = True
if is_logged_in:
    print("Welcome Back!")

#! Python can evaluate many types of values as True or False in an if statement.
#* Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.
#* This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).



