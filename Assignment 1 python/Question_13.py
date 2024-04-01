''' Question 13
Write a Python program to calculate the area of a rectangle given its length and width. (Assume length and width are provided as inputs.)

Ans:-
1 output=>
Enter length: 12.4
Enter width: 16.3

2 And final Output is =>202.12



'''
# Take input for length and width of rectangel
length = eval(input("Enter length: "))
width = eval(input("Enter width: "))

# Defining function to calculate the area
def area(l, w):
    return l*w
print(area(length, width))