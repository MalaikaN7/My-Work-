import math

# Ask the user to choose which calulcation they want, investment or bond.
investment = input("Please enter the type of calculation you wish to review \
a-investment or b-bond: ").lower()

# This is a formula to calculate their investment\
# as simple interest or compound.
if investment == "a":
    principle_amount = float(input("Please enter your investment amount: "))
    interest = int(input("Please enter your interest rate: "))
    time = float(input("Please enter the total time in years if simple or \
months if compound: "))
    
    user_interest = input("Please enter the type of investment you are \
looking to make c-simple interest or d-compound interest: ")
    
    if user_interest == "c":
        print(round(principle_amount * (1 + (interest/100) * time)), 2)
        
    if user_interest == "d":
        print(round(principle_amount * math.pow(1 + (interest/100), time)), 2)

# If the user chose bond this formula calculates the amount\
# they have to repay based on their house va;ue, interest and time.
elif investment == "b":
    house_value = float(input("Please enter your house valuet: "))
    interest = (float(input("Please enter your interest rate: "))/100)/12
    time = float(input("Please enter the total months of your bond : "))

# Print out the repayment amount based on the\
# formula to calculate their bond repayment.
    print(round((interest * house_value) / (1 - (1+interest) ** (-time))), 2)
