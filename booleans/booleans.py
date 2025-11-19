# Booleans represent one of two values: True or False.

#? When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(9>5) #? Returns True
print(9<3) #? Returns False
print(9==4) #? Returns False

#? (Every empty, None, 0, False) values returns False
#? For example, They returns False
a = ""
b = False
c = 0
d = None
e = [] #? Empty list
f = () #? Empty tuple
h = set() #? Empty set
i = {} #? Empty dictionary

#? (Every empty, None, 0, False) except returns True
#? For example, They returns True
x = "hello"
y = True
z = 1
k = ["apple"] #? a list with a single value
l = ("apple",) #? a tuple with a single value
m = {"apple"} #? a set with a single value
n = {"fruit":"apple"} #? a dictionary with a single value(key=value)pair
print(type(k))
print(type(l))
print(type(m))
print(type(n))

#? In python, all condition returns boolean value: True or False
if i: # i is an empty dictionary, so it returns False and that's why else will excecute
    print("Right")
else:
    print("Wrong")