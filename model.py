
rate = float(input("Enter  the rate: "))
time = float(input("Enter the time: "))
principal = float(input("Enter the principal: "))

amount = principal *  (pow((1 + rate/100),time))
ci  =  amount  -  principal
print("Compound  interest  is   ",ci)


def compound_interest(principal, rate, time):
    # Calculate the amount using the compound interest formula
    amount = principal * (pow((1 + rate / 100), time))
    
    # Calculate the compound interest
    ci = amount - principal
    
    return ci

# Example usage
principal = 1000  # Principal amount in dollars
rate = 6       # Annual interest rate (e.g., 10.25%)
time = 2           # Time in years

# Calculate compound interest
ci_amount = compound_interest(principal, rate, time)

# Print the result
print(f"Compound interest is ${ci_amount:.2f}")

import pandas as pd

data = pd.read_csv("Dataset.csv")
