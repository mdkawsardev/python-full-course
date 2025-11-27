# Python Else Statement
#? The Else Keyword
#* The else keyword catches anything which isn't caught by the preceding conditions.
#* The 'else' statement is executed when the 'if' condition (and any 'elif' conditions) evaluate to False.
score = 0
if score >= 90 and score < 100: #* Condition is False
    print("Grade Golden") #* Python skips
elif score >= 80 and score < 90: #* Condition is False
    print("Grade A") #* Python skips
elif score >= 70 and score < 80: #* Condition is False
    print("Grade A-") #* Python skips
elif score >= 60 and score < 70: #* Condition is False
    print("Grade B") #* Python skips
elif score >= 50 and score < 60: #* Condition is False
    print("Grade C") #* Python skips
elif score >= 40 and score < 50: #* Condition is False
    print("Grade D") #* Python skips
else: #* If all conditions are False
    print("You're failed") #* This statement is executed

#* In these conditions. All conditions are false, so 'else' statement is executed

#? Else Without Elif
#* You can also have an else without the elif:
a = 9
b = 8
if a < b:
    print("A is less than B")
else: 
    print("A is greater than B")
#* This creates a simple two-way choice: if the condition is true, execute one block; otherwise, execute the else block.

#? How Else Works
#* The else statement provides a default action when none of the previous conditions are true. Think of it as a "catch-all" for any scenario not covered by your if and elif statements.
#! Note: The else statement must come last. You cannot have an elif after an else.

number = 4
if number % 2 == 0:
    print("It's an even number")
else:
    print("It's an odd number")

#? Else as Fallback
#* The else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.
user = "imran"
if len(user) > 0:
    print(f"Welcome, {user}")
else:
    print("Empty field is not acceptable")