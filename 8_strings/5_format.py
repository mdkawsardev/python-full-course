# String Format
#? As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

#? This will produce an error:
# age = 23
# txt = "My name is Imran, I am " + age
# print(txt)
#? We can simply use f-string
#? To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 23
txt = f"My name is Imran, I m {age}"
print(txt)

#? Display the price with 2 decimals:
price = 69
product = f"This is a computer and its cost: {price:.2f}" #? .2f creates two floating point after the value. Result is 69.00
print(product)

# Placeholders and Modifiers
#? A placeholder can contain variables, operations, functions, and modifiers to format the value.
#? A placeholder can contain Python code, like math operations:
#? {placeholder}


