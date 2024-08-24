# *** Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
import math
taken_number= int(input("Enter the number" ))
square= taken_number**2
cube= taken_number**3
print(square)
print(cube)
sq= -4**2
cu= 8**3
print("The square of the number is", sq)
print("The cube of the number is", cu)




# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1= int(input("Enter the first number"))
num2= int(input("Enter the second number"))
if num1 > num2:
    print("The first number is greater than the second number", num1)
else:
    print("The Second number is greater than the first number", num2)
if num1 < num2:
    print("The first number is less than the second number", num1)
else:
    print("The Second number is less than the first number", num2)
if num1 == num2:
 print("The first number is equal to the second number", num1)
else:
 print("The first number is  not equal to the second number", num2)
