# Unpack Tuples
#? When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#* Packing a tuple:
tuple1 = ("January", "February", "March", "April")
print(tuple1)

#* But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
#* Unpacking a tuple:
(first_month, second_month, third_month, fourth_month) = tuple1 #* I assigned value to the variable
print(first_month) #* This contains "January"
print(second_month) #* This contains "February"
print(third_month) #* This contains "March"
print(fourth_month) #* This contains "April"

#! Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

#? Using Asterisk*
#* If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

(f_month, s_month, *th_month) = tuple1
print(f_month)
print(s_month)
print(th_month)
#* I can use asterisk on any variable
(one, *two, three) = tuple1
print(one)
print(two)
print(three)