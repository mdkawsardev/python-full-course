# Python Datetime
#? Python Dates
#* A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
#* Import the datetime module and display the current date:
import datetime as date
time = date.datetime.now()
print(time) #* Prints the current date

"""
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:
"""
Year = date.datetime.now().year
print(Year)

#? Creating Date Objects
#* To create a date, we can use the datetime() class (constructor) of the datetime module.
#* The datetime() class requires three parameters to create a date: year, month, day.
#* Create a date object:
created_date = date.datetime(2018, 3, 23)
print(created_date)

#? The strftime() Method
#* The datetime object has a method for formatting date objects into readable strings.
#* The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

day = time.strftime("%A") #* Wednesday
print(day)
month = time.strftime("%B") #* December
print(month)
number_of_week = time.strftime("%W") #* 48/ number of week
print(number_of_week)
full_date = time.strftime("%D") #* 12/03/25
print(full_date)
full_date = time.strftime("%I") #* Just date
print(full_date)
x = time.strftime("%R")
print(x)
#! All resources are available on W3School
