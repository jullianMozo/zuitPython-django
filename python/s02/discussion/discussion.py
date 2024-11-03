#  user input
#  promt()
#  input allows us to gather data from the user input,
# returns "string" type
 
#  "\n" stands for line break
 
# username = input("please enter youre name:\n") 
# print(f"Hi {username}! Welcome to python short course")

# num1 = input("Enter 1st number:\n")
# num2 = input("Enter 2st number:\n")
# print(f"The sum of num1 and num 2 is {num1 + num2}")

# num1 = int(input("Enter 1st number:\n"))
# num2 = int(input("Enter 2st number:\n"))
# print(f"The sum of num1 and num 2 is {num1 + num2}")

# num1 = input("Enter 1st number:\n")
# num2 = input("Enter 2st number:\n")
# print(f"The sum of num1 and num 2 is: {int(num1) + int(num2)}")

# with the user input user can give inputs for the prograM
# to control the application using control structures

# Control Structure can be divided into selection and repitition structure

# selection control structure allows the program to choose ammong
# the choices and run specific codes dependeing on the choice taken

# repitition control structure allows the program to repeat the certain
# block of code a given condition and terminating condition

# If=else Statements
# are used to choose between two or more code block depending on the condition

# Declare a variable to use for the condtional statement
# test_num = 75

# if test_num >= 60:
#     print("test passed")
# else: print("test failed")

#  If-else chains - can also be used to have more than 2 choices
# for the program

# test_num2 = int(input("please enter the 2nd test number:\n"))

# if test_num2 > 0:
#     print("test number is positive")
# elif test_num2 ==0:
#     print("the number is zero")
# else:
#     print("The number is negative")   


# mini activity
# create a if else statement that determines 
# if a number is disivisble by both 3,5 or both



# test_num3 = int(input("please enter the 2nd test number:\n"))

# if (test_num3 % 3 == 0) and (test_num3 % 5 == 0):
#     print("the number is divisible both 3 and 5")
# elif test_num3 % 3 == 0:
#     print("the number is divisible by 3")
# elif test_num3 % 5 == 0:
#     print("the number is divisible by 5") 
# else:
#     print("the number is not divisible by 3 or 5")   


# Loops
# Python can repeat block of code

# While loop - use to execute  a set of statement as long as athe condition is true
# initial value i, while = condition, print = code, i+= iterarte  

# i = 1       
# while i <= 5:
#     print(f"current count is {i}")
#     i+=1


# for Loops - are used for iterating over a sequence

# fruits = ["apple", "banana", "cherry"]

# for indiv_fruit in fruits:
#     print(indiv_fruit)



# range() method
# to used the fro loop to iterate through values the range method can be use
# 
# syntax
# range(stop)
# range(start,stop)
# range(start,stop,step)


# for x in range(6):
    #  print(f"the current value is {x}")
# for x in range(2, 20, 2):
#     print(f"the current value is {x}")


# break and continue statement

# Break statement - used to stop the loop

# j =1 
# while j < 6:
#     print(j)
#     if j == 3:
#         break
#     j+= 1

# Continue statement - 


# k = 1
# while k < 6:
#     k += 1
#     if k == 3:
#         continue
#     print(k)