year = int(input("input a year:\n"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
     print(f"{year} is a leap year")
else:
     print(f"{year} is not a leap year")



rows = int(input("Enter number of rows:\n"))
columns = int(input("Enter number of columns:\n"))

for i in range (rows):
    for j in range (columns):
        print("*", end="")
    print()
       
        
