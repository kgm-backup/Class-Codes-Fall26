'''
Write a program that calculates discount based on the amount of purchase. Ask the
user for the purchase amount and apply the following discount rates:
    No discount if the amount is less than equals to 50
    10% discount if the amount is between 50 and 100
    20% discount if the amount is equal to or over 100
You need to report to the user the final amount after discount. Also tell them how
much discount was applied in percent.

Variable Declaration
    InitialAmount - Float
    FinalAmount - Float
    DiscApplied - Integer

We will take InitialAmount as Input
        NEED TO CONVERT THE INPUT TO FLOAT

After taking the input, I need to figure out which category it falls in
        Conditional/IF statements shall be used
'''

# DECLARE InitialAmount, FinalAmount : FLOAT
# DECLARE DiscApplied : INTEGER

InitialAmount = float(input("Please enter your total: "))

if InitialAmount <= 50:
    print("No Disc Applied!")
elif InitialAmount > 50 and InitialAmount < 100:
    FinalAmount = InitialAmount * 0.9
    # print("10% Discount applied. Your new total is:", FinalAmount)
    print(f"10% Discount applied. Your new total is: {FinalAmount}")
elif InitialAmount >= 100:
    FinalAmount = InitialAmount * 0.8
    print("20% Discount applied. Your new total is:", FinalAmount)
else:
    print("Please enter a valid amount")