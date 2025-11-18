# Casting in Python
x = "9"
y = 33
z = 9.033
k = 2j

#? Casting with str() constructor
string1 = str(x)
string2 = str(y)
string3 = str(z)
string4 = str(k)
print(type(string1))
print(type(string2))
print(type(string3))
print(type(string4))

#? Casting with int() constructor
int1 = int(x)
int2 = int(y)
int3 = int(z)
print(type(int1))
print(type(int2))
print(type(int3))

#? Casting with float() constructor
flaot1 = float(x)
flaot2 = float(y)
flaot3 = float(z)
flaot4 = float(z)
print(type(flaot1))
print(type(flaot2))
print(type(flaot3))
print(type(flaot4))

#? Casting with complex() constructor
com1 = complex(x)
com2 = complex(y)
com3 = complex(z)
com4 = complex(k)
print(type(com1))
print(type(com2))
print(type(com3))
print(type(com4))