# Strings in python are surrounded by either single quotation marks, or double quotation marks.
#? 'hello' is the same as "hello".
print("hello")
print('hello')
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
a = "I'm a web developer" #? single quote is allowed inside of double quotes
b = 'I am a "developer"' #? double quote is allowed inside of single quotes

#? Wrong practice
# a = 'I'm a web developer'
# b = "I am a "developer"" 


#? You can assign a multiline string to a variable by using three quotes:
c = """
twinkle twinkle 
little stars
how above...
"""
# You can aslo use '''''' single quotes
c = '''
twinkle twinkle 
little stars
how above...
'''

# To know the lenth of a string, I will use len() method
name = "imran khan is a programmer"
print(len(name))

#? Accessing single charachter by index number
print(name[0])
print(name[1])
print(name[2])
print(name[3])

#? Now, I will use a for-loop
for i in name:
    print(i)

#? Check if "programmer" is present in the following text:
print("programmer" in name) # It will return True, becuase "programmer" is in the name variable
print("programmers" in name) # It will return False, becuase "programmer" is not in the name variable
#? Another way
if "programmer" in name:
    print("Yes! programmer is available")
else:
    print("No! programmer is not available")

#? To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
print("programmer" not in name) # It will return False
print("programmers" not in name) # It will return True
if "programmer" not in name:
    print("programmer is not in the name variable")
else:
    print("programmer is in the name variable")