'''Question 9
List three functions that can be used to obtain the integer, floating-point number, or string version of a value.

Ans:-Three functions you can use to obtain the integer, floating-point number, or string version of a value are:
- int(x): This function converts the value x to an integer.
- float(x): This function converts the value x to a floating-point number.
- str(x): This function converts the value x to a string representation.

'''
#Code
x = 15.5
print(int(x))
print(float(x))
print(f"Variable x has type {type(str(x))}")

#And Output is :-
'''
15
15.5
Variable x has type <class 'str'>'''