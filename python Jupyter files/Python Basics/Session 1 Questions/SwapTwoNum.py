#Take 2 numbers as input from the user.
## Write a program to swap the numbers without using any special python syntax.

# Take Two Number from User
num1 = input("Enter the First Number")

num2 = input("Enter the Second Number")

# print that numbers before swapping 
print("the Numbers before swapping")
print("The num1 is " , num1)
print("The num2 is " , num2)

# Swapping the numbers

num3 = num1 
num1 = num2 
num2 = num3

# print the result after swapping 

print("the numbers after swapping are ") 
print("the num1 is : " , num1 )
print("the num2 is : " , num2 )