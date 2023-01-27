
# Find the Sum of a 3 digit number entered by user

# e.g : 
# input : 345
# add : 3+4+5 
#output : 12

#take input from user 

num = int(input("Enter 3 digit Number"))
print(num)

# we have to seprate that 3 digit number.
# use modulas operator and modulas that number by 10

# 345 % 10  -> 5
a = num%10

#using that we can get last digit
#
num = num // 10
# 34 % 10 -> 4
b = num % 10

num = num // 10
# 3 % 10 -> 3
c = num % 10

print(a + b +c)