# Python Match
#? The match statement is used to perform different actions based on different conditions.

#* The Python Match Statement
#* Instead of writing many if..else statements, you can use the match statement.
#* The match statement selects one of many code blocks to be executed.

"""
! Syntex
match expression:
    case x:
        code block
    case y:
        code block
    case z:
        code block

! This is how it works:
. The match expression is evaluated once.
. The value of the expression is compared with the values of each case.
. If there is a match, the associated block of code is executed.
"""

#? Example
day = 3
match day:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuesday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thursday")
    case 7:
        print("Friday")
    case _: #* This is a default value
        print("Searching day...")

#* Default Value
#* Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
#* The value _ will always match, so it is important to place it as the last case to make it behave as a default case.

#? Combine Values
#* Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
holiday = 3
match holiday:
    case 1 | 2 | 3 | 4 :
        print("Holiday's going on")
    case _:
        print("Working days")

#? If Statements as Guards
#* You can add if statements in the case evaluation as an extra condition-check:
month = 3
eid_day = 18
match eid_day:
    case 16 | 17 | 18 if month == 3:
        print("Enjoy Eid days")
    case _:
        print("End days have ended")

