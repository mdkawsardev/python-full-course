# When we write python code we need to use escape character
#? An escape character is a backslash \ followed by the character you want to insert.
#?An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

# txt = "We found a weapon cache sounds got "michiel"" #? This is a wrong procedure
txt = "We found a weapon cache sounds got \"michiel\"" #? This is correct procedure. \" double quote
print(txt)
# title = 'we found a 'nuclear'' #? This is a wrong procedure
title = 'we found a \'nuclear\'' #? This is a correct procedure. \' single quote
print(title)
print("My name is Imran\nI'm a programmer\nI need to learn something new\nAll about me") #? \n starts a new line
print("Hello\\How are your?\\It's time to write code\\") #? \\ backslash
print("Application\n\tYour application has been submitted") #? \t tab
print("im\bspace\bt") #? \b backspace
