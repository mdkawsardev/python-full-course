# Specify the start index and the end index, separated by a colon, to return a part of the string.
#? Get the characters from position 2 to position 5 (not included):
a = "Hello World"
print(a[2:5]) #? Result is -> llo, here 2 is included but 5 is excluded
print(a[0:4]) #? Result is -> Hell, 0 means from starting to 4(excluded)
print(a[:4]) #? Resuld is -> Hell, same as above
print(a[6:]) #? Result is -> World, [6:0] starts from 6 index to end of the line

#? Negative slicing
print(a[-5:]) #? Result is -> World. It starts counting from the end of the line
"""
Negative index
d = -1 it's always excluded
l = -2
r = -3
o = -4
W = -5
"""
print(a[-5:-1]) #? Result is -> Worl, beacuse -1 index is excluded, here d = -1, so d is excluded

"""
?Positive indexes
H = 0
e = 1
l = 2
l = 3
o = 4
whitespace = 5
W = 6
o = 7
r = 8
l = 9
d = 10
? Negative indexes
d = -1
l = -2
r = -3
o = -4
W = -5
whitespace = -6
o = -7
l = -8
l = -9
e = -10
H = -11
"""
print(a[-11:-10]) #? Result is -> H, -10 index is exluded