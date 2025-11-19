# Assignment Operators
#? Assignment operators are used to assign values to variables:

"""
? =                   x = 5                   x = 5
? +=                  x += 5                  x = x + 5
? -=                  x -= 5                  x = x - 5
? *=                  x *= 5                  x = x * 5
? /=                  x /= 5                  x = x / 5
? %=                  x %= 5                  x = x % 5
? //=                 x //= 5                 x = x // 5
? **=                 x **= 5                 x = x ** 5
? :=                  x := 5                  x = 5
"""
#? A normal expression
txt = "Hello"
count = len(txt)
if count > 3:
    print("Content is greater than 3")
#? A walrus operator expression
if (count := len(txt) > 3):
    print("Content is greater than")

#* Both of them output is same, difference a normal expression and a walrus operator's expression