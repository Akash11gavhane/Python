# Write a program to find the euclidean distance between two coordinates.
## Take both the coordinates from the user as input.

# take input from user 
import math

print("Enter x1 and x2 for point A ") 
x1 , x2 = map(int , input().split())

print("Enter y1 and y2 for point b")
y1 , y2 = map(int , input().split())

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("The euclidean Distance between A and B is : " , dist)