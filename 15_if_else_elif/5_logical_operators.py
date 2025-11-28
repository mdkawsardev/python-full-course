# Logical operators in Python
#? Logical operators are used to combine conditional statements. Python has three logical operators:
"""
and                 Returns True if both statements are True
or                  Returns True if one statement is True 
not                 Reverse the result, returns False if result is True
"""
#? The and Operator
a = 4
b = 9
if a > 0 and b < 10:
    print("Both conditions are True")
else: 
    print("Condition is False")

#? The or Operator
x = 31
y = 40
if x > 0 or y > 50:
    print("Condition is True")
else:
    print("Condition is False")

#? The not Operator
k = 30
i = 40
if not k > i:
    print("Reverses the condition")
else:
    print("Something")

#? Combining Multiple Operators
#* You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.

if (a > b or x < y) and (k > i or k < x):
    print("Condition is True")
else:
    print("Condition is False")