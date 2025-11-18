# Numbers in Python
"""
#? There are three numeric types in Python:

int
float
complex
"""
#? There are three numeric types in Python:

x = 1 # Int
y = 1.00 # Float
z = 1j # Complex

# To know types of these, I will use type() method
print(type(x))
print(type(y))
print(type(z))

#? Integer
x = 1
y = 23482309840923840923
z = -23232
print(type(x))
print(type(y))
print(type(z))

#? Float
x = 1.324
y = 0.3332
z = -121.343
k = 3343e53
l = 332E53
m = -232.33e343
print(type(x))
print(type(y))
print(type(z))
print(type(k))
print(type(l))
print(type(m))

#? Complex
x = 3 + 5j
y = 4j
z = -3j
print(type(x))
print(type(y))
print(type(z))

#? Type Conversion
x = 1
y = 1.03
z = 7j

a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))