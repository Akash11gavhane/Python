
# Print The following Pattern.

#  *
#  * * 
#  * * * 
#  * * * *
#  * * * * *

nrow = int(input("Enter the Number of rows"))
for i in range(1 , nrow+1):
    for j in range(1 , i+1):
        print("*" , end = ' ')
    print()