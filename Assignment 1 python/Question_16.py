'''Question 16
Create a Python program that takes the radius of a circle as input and calculates its area. (Assume the value of pi is 3.14.)

Ans:-Output:-Enter radius of circle: 12
            452.16
'''
# Create variable for pi
pi = 3.14
# Take input from user
radius = eval(input("Enter radius of circle: "))
area = pi * radius * radius
print(round(area, 2))