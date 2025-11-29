# Python For Loops
#? A 'for' loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#* This is less like the 'for' keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#* With the 'for' loop we can execute a set of statements, once for each item in a list, tuple, set etc.

#? Print each fruit in a fruit list:
fruits = ["Apple", "Banana", "Cherry", "Melon", "Watermelon"]
for x in fruits:
    print(x)
#* The 'for' loop does not require an indexing variable to set beforehand.
#? Looping Through a String
#* Even strings are iterable objects, they contain a sequence of characters:
name = "kawsar"
for n in name:
    print(n)

#? The break Statement
#* With the 'break' statement we can stop the loop before it has looped through all the items:
#* Exit the loop when x is "Melon":
for x in fruits:
    print(x)
    if x == "Melon":
        break

#* Exit the loop when x is "Melon", but this time the 'break' comes before the print:
for x in fruits:
    if x == "Melon":
        break
    print(x)

print("")
#? The continue Statement
#* With the 'continue' statement we can stop the current iteration of the loop, and continue with the next:
for x in fruits:
    if x == "Melon":
        continue
    print(x)

#? The range() Function
#* To loop through a set of code a specified number of times, we can use the 'range()' function,
#* The 'range()' function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(10):
    print(x)
#* Note that range(10) is not the values of 0 to 10, but the values 0 to 9.
#* The 'range()' function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(1, 10):
    print(x)
#* The 'range()' function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
print("")
for x in range(2, 30, 3):
    print(x)

#? 'Else' in For Loop
#* The 'else' keyword in a 'for' loop specifies a block of code to be executed when the loop is finished:
#* Print all numbers from 0 to 5, and print a message when the loop has ended:
print("")
for x in range(6):
    print(x)
else:
    print("Finally finished!")
#! Note: The 'else' block will NOT be executed if the loop is stopped by a 'break' statement.
#* Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

#? Nested Loops
#* A nested loop is a loop inside a loop.
#* The "inner loop" will be executed one time for each iteration of the "outer loop":
#* Print each adjective for every fruit:
print("")
adj = ["Big", "Small", "Medium"]
for x in adj:
    for y in fruits:
        print(x, y)

#? The pass Statement
#* 'for' loops cannot be empty, but if you for some reason have a 'for' loop with no content, put in the pass statement to avoid getting an error.
for x in range(10):
    pass
