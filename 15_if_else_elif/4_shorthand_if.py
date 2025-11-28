from random import randint
# Python Shorthand If
#? Short Hand If
#* If you have only one statement to execute, you can put it on the same line as the if statement.
#* One-line if statement:

a = 4
b = 5
if b > a: print("B is greater than A")
#! Note: You still need the colon : after the condition.

#? Short Hand If ... Else
#* If you have one statement for if and one for else, you can put them on the same line using a conditional expression:
#* One-line if/else that prints a value:
print("A is less than B") if a < b else print("B is greater than A")
#!This is called a conditional expression (sometimes known as a "ternary operator").

#? Assign a Value With If ... Else
#* You can also use a one-line if/else to choose a value and assign it to a variable:

a = 5
b = 3
c = a if a > b else b
print(f"Bigger is {c}")

#? Multiple Conditions on One Line
#* You can chain conditional expressions, but keep it short so it stays readable:
#* One line, three outcomes:

x = 33
y = 33
print("K") if x > y else print("They are equal") if x == y else print("They are not equal")

#? Practical Examples
#* Ternary operators are particularly useful for simple assignments and return statements.
#* Finding the maximum of two numbers:

k = randint(1, 20)
i = randint(1, 20)
big_one = k if k > i else i
print(f"Big number is: {big_one}, between k or i")
print(f"This is from k {k}")
print(f"This is from i {i}")

#? Setting a default value:
username = ""
name = username if username else "Guest"
print(f"user name is: {name}")

#? When to Use Shorthand If
#* Shorthand if statements and ternary operators should be used when:
"""
The condition and actions are simple
It improves code readability
You want to make a quick assignment based on a condition
"""
#! Important: While shorthand if statements can make code more concise, avoid overusing them for complex conditions. For readability, use regular if-else statements when dealing with multiple lines of code or complex logic.

