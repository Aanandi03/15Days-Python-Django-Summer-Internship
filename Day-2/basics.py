# COMMENTS IN PYTHON

# Hash is used to comment in the Python
''' Inverted comma are also used to comment in python '''

# This is a single line comment!
""" 
This is a multi-line comment.
Generally, used to show documentation.

"""

# VARIABLES IN PYTHON

week_days = 7 # declaration of varaible
day_hours = 24

week_hours = (week_days * day_hours)


print(week_hours) # print values of variable

# DATATYPES IN PYTHON

#Int Str Float Bool

x = 10  
y = "10"
z = 10.1

sum1 = x+x
sum2 = y+y

print(sum1,sum2)
print(type(x),type(y),type(z))

#Complex

n=10 + 2j
print(type(n)) 

#List
#Represent arrays of values that may change during the course of the program:

student_grades = [3.0, 5.0, 4.5] 
print(student_grades)
print(type(student_grades))

#Creating a complex list

rainfall = [10.1, 9, "no data", [1,2,3]] 
print(rainfall)
print(type(rainfall))

#Range
#To specify the list boundaries
print(list(range(1, 10, 2))) 

#Dictionary
#Represent pairs of keys and values:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}  
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

phone_numbers.keys()
phone_numbers.values()

# Tuples
# Represent arrays of values that are not to be changed during the course of the program:

vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(vowels)
print(one_digits)

# Set
# Used to store multiple items in a single variable and it's iterable,
# mutable and no duplicate values:

s={4,5,6,90,110,0}
print(s)

# Slice/Split
# Used to access elements in it:

#List

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days)
print(days[1:4])#In a list, the 2nd, 3rd, and 4th items can be accessed with
print(days[:3])#First three items of a list:
print(days[-3:])#Last three items of a list:
print(days[:-1]) #Everything but the last:


