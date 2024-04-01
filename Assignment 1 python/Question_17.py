'''Question 17
Write a Python program to find the maximum of two numbers entered by the user.

Ans:-Output(Enter first number: 12
Enter second number: 32
Greater number is 32)
'''

# Taking input from user
num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))

if num1 > num2:
    print(f"Greater number is {num1}")
else:
    print(f"Greater number is {num2}")