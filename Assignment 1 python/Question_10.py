''' Question 10
Explain why the following expression causes an error and suggest how to fix it:<br>
'I have eaten ' + 99 + ' burritos.'

Ans:-# The given expression throws a TypeError stating that str can't be concatinated with int
# This can be fixed by presenting 99 as string literal instead of integer.
'I have eaten ' + '99' + ' burritos.'

Output :-'I have eaten 99 burritos.'
'''