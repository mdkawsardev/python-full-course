# Python Elif Statement
#? The Elif Keyword
#* The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#* The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
a = 999
b = 99
if a == b:
    print("A and B are equal")
elif a > b:
    print("A is greater than B")
#* A is not equal B so first condition is False then go to the second condition. In second condition A is greater than B, so condition is True now, this is executed

#? Multiple Elif Statements
#* You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.
#* Testing multiple conditions:

score = 67
if score >= 90 and score < 100: #* Condition is False
    print("Grade Golden") #* Python skips
elif score >= 80 and score < 90: #* Condition is False
    print("Grade A") #* Python skips
elif score >= 70 and score < 80: #* Condition is False
    print("Grade A-") #* Python skips
elif score >= 60 and score < 70: #* Condition is True
    print("Grade B") #* This block of code is executed
elif score >= 50 and score < 60:
    print("Grade C")
elif score >= 40 and score < 50:
    print("Grade D")

#? How Elif Works
#* When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
#! Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.


