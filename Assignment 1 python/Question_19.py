''' Question 19
Write a Python program that prompts the user to enter a number and then prints whether the number is positive, negative, or zero.

Ans:- Output(Enter number: 15
Entered number 15 is positive)
'''
# Taking input from user
num = eval(input("Enter number: "))
if num > 0:
    print(f"Entered number {num} is positive")
elif num == 0:
    print(f"Number is 0")
else:
    print(f"Entered number {num} is negative")