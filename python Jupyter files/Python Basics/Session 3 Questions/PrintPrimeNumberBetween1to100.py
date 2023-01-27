
# print prime numbers between 1 to 100

# see the logic for finding prime number on youtube

# we take lower range and upper range from user

lower = int(input("enter lower range"))
upper = int(input("Enter upper range"))

for i in range(lower , upper+1):
     for j in range(2 , i ):
        if i % j == 0 :
            break
        else:
            print(i)