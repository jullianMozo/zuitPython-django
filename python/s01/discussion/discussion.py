# comments
# comments in python are done using "#" symbol

# Python syntax
# print "hello world" in python
print("hello world")

# indentaion
# Where in other programing languages the indentation in python
# is very important 
# in python , indentation is use to indicate a block of code
# similar to js. there is no need to end statements with semi colon


# naming convention 
# python uses snake case convention full_name

# the terminology used for variable name is identifier
# all identifiers should begin with a letter a-z, or an underscore "_"
# after first character , identifier can have a combination of character
#  a keyword cannot be used as an identifier
#  identifier are case sensitive
age = 35;
middle_initial = "C";
# AGE = 85;
# python allows aigning of values to multiple variable in 1 line

name1, name2, name3, name4, = "john", "paul", "george", "ringo"

# data types
# 1. String (str) -  for alphanumeric and symbols
full_name = "john doe"
secret_code = "pa$$w0rd"
# 2. Numbers (int, float, complex) - for integers, decimals, complex numbers

num_of_days =  365
# this is an integer

pi_approx = 3.1416
# this is a decimal

complex_num = 1 + 5j 
# this is a complex number, j represent imaginary component

# 3. Boolean (bool) - for truth values
# boolean values in python starts with uppercase letter

is_learning = True
is_difficult = False

# using variable
# use variable concatination ("+" symbol between strings can be use)
print("my name is " + full_name)

#  print("my age " + age)
# typecasting 
print("my age " + str(age))

# there maybe times when you wnat to specify a type on a variable. 
# this can be done with casting

#  1.  int() - converts value to integer values
#  2. float() - conerts value into a float values
#  3. str() - converts value into a string values

print(int(3.5))
print(int("9876"))

# another way to avoid the error in printing without the use of typecasting
# use f-string
# to use f string, add a lower case "f" before the string 
# and place the desired variablr in {}

print(f"Hi my name is {full_name} and my age is {age}")

# Operations
# python has operator families taht can be used to manipulate variables

# arithmetic operators - performs mathematical operations
print(1 + 8)
print(15 - 8)
print(18 * 9)
print (21 / 7)

# get the modulo
print(18 % 4)
print(2 ** 6)

# aasingment operators - used to assigned values to out variables
# addition assingment operator
num1 = 3
num1 += 4
print(num1)
#  other operator include -=, *=, /=, %=
num1 -= 4
print(num1)
num1 *= 4
print(num1)
num1 /= 4
print(num1)
num1 %= 4
print(num1)

print(1 == 1)
# True
print(5 > 10)
# False
print(5 < 10)
# True
print(1 <= 1)
# True
print(2 >= 3)
# False
print(1 != 1)
# False

# Logical Operators - used to combine conditional statements
print(True and False)
# false
print(False or True)
# true
print(not False)
# true