# Nested If Statements
#? You can have if statements inside if statements. This is called nested if statements.

x = 50
if x > 20:
    print("x is greater than 20")
    if x > 30:
        print("x is greater than 30")
        if x > 40:
            print("x is greater than 40")
        else:
            print("x is less than 40")
    else:
        print("x is less than 30")
else:
    print("x is less than 20")