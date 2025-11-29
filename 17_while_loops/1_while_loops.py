# Python While Loops
#? Python Loops
#* Python has two primitive loop commands:
"""
'while' loops
'for' loops
"""

#? The while Loop
#* With the 'while' loop we can execute a set of statements as long as a condition is true.
#* Print k as long as k is less than or equal 10:
k = 0
while k <= 10:
    print(k, "point")
    k += 1
#! Note: remember to increment i, or else the loop will continue forever.

#? The break Statement
#* With the 'break' statement we can stop the loop even if the while condition is true:
i = 0
while i < 10:
    print(i)
    if i == 6: #* if i is 6 the loop will stop
        break
    i += 1

#* This will print all even numbers
l = 0
while l < 50:
    l += 1
    if (l % 2 != 0):
        continue
    print(l, "Even number")

print("")
#* This will print all odd numbers
l = 0
while l < 50:
    l += 1
    if (l % 2 == 0):
        continue
    print(l, "Odd number")

#? The 'else' Statement
#* With the 'else' statement we can run a block of code once when the condition no longer is true:
#* Print a message once the condition is false:
count = 0
while count <= 20:
    print(count)
    count += 1 #* count = count + 1
else:
    print("Counting ended! Nothing is less than or equal 20")
