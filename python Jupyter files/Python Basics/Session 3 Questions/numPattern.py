# print the following pattern

# 1
# 1 2 1
# 1 2 3 2 1 
# 1 2 3 4 3 2 1

nrow = int(input('Enter the Number of rows'))

for i in range(1 , nrow+1):
    for j in range(1 , i+1):
        print(j , end=' ')
    for k in range(i-1 , 0 , -1):
        print(k , end=' ')
    print()
