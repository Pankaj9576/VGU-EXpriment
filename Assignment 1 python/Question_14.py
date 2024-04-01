''' Question 14
Create a Python program that asks the user for their age and prints out a message saying whether they are a child, teenager, or adult based on their age.

Ans:-
output=Enter your age: 18
       You are a teenager.
'''
# Take input from user
age = eval(input("Enter your age: "))

if age < 12:
    print("You are a child.")
elif age <= 18:
    print("You are a teenager.")
else:
    print("You are a adult.")