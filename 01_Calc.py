# Any line in python that starts with a hash is a comment!
# A comment is a line that is not a part of your code, its smth that just exists there as plaintext
'A special thing about python is that anything that is written in speechmarks and not assigned to a'
"variable is also essentially treated as a comment"
'''
HOWEVER, YOU CAN NOT USE THIS METHOD OF COMMENTING IN YOUR EXAM!!! THIS IS ONLY FOR ME TO ADD VARIETY

How to run code in python?
        1. Open terminal
        2. write 
                python <filename>.py
How to print smth in Python
'''
# print("Hello World!")

'''
Write a simple calculator that asks the user for two numbers and an operator 
(+, -, *, or /), then displays the result. 

Unlike pseudocode, Python does not need variable declaration. HOWEVER, you are still expected to declare
variable in comments 

How many many variables do we need?
        Num1
        Num2
        Operator
    3 variables needed in total

User input needed!

Based on the user's input, we need to decide if we want to add/subtract etc
    USE IF CONDITIONS!
'''

# DECLARE num1, num2, Result : INTEGER
# DECLARE operator : STRING

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# Lets try and test the code before we move on
# print(num1)
# print(num2)
# Input seems to be working fine so far

'Lets try adding these numbers'
# Result = num1 + num2
# print(Result)

'''
How does 3+5 equal 35?
Concatenation happened -> when two STRINGS are joined together
Since + is also the concatenation operator in python, what is happening is that
our inputs are being concatenated

This means that our input is actually being treated as a string instead of a number(integer) 
'''

# In Python all inputs are treated as strings by default
'How can we take input as an integer?'

"________________________________________________________________________________________________"

# DECLARE num1, num2, Result : INTEGER
# DECLARE operator : STRING

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

# Result = num1 + num2
# print(Result)

operator = input("Enter an operator from +-*/: ")

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("Invalid operator")