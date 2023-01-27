

#Write a program to find the simple interest when the value of principle,##rate of interest and time period is provided by the user.

# Write your code here

principle_amount = int(input("Enter the principle Amount : "))

rate_of_intrest = float(input("Enter the rate of intrest : "))

time_period = int(input("enter the duration : "))

simple_interest = (principle_amount * rate_of_intrest * time_period) / 100

print("the simple intrest is : " , simple_interest)