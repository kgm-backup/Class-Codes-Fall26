'''
Given a number you need to tell whether it is even or odd

To check if  number is even or odd, we divide it by 2. Then we check the remainder
of this division.
If the remainder is 0 -> number is even

In programming languages, we have a special operator for remainder. It is called the modulus operator and
is represented in Python using the % sign
'''

# DECLARE UserIn : INTEGER
UserIn = int(input("please enter a number"))

if UserIn % 2 == 0:
    print("Even")
else:
    print("Odd")

'''
user will input an integer, you need to check if the User wins or not. Winning
condition: The number should be even and greater than 500
'''
UserGuess = int(input("Please enter a number: "))
if UserGuess > 500 and UserGuess % 2 == 0:
    print("You win")
else:
    print("You lose!")