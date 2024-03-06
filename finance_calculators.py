import math

# Opening selection of investment vs bond
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print("\n")
calculation_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
calculation_selection_lower = calculation_selection.lower()

# investment - inputs from user required
if calculation_selection_lower == "investment":
    deposit = float(input("Please enter your deposit amount: "))
    interest_rate_investment = float(input("Please enter the interest rate: "))
    total_years = float(input("How many years do you plan on investing?: "))
    interest_type = input("Would you like simple or compound interest?: ")

# simple interest calculation
    if interest_type == "simple":
        simple_interest_calculation = deposit * (1 + ((interest_rate_investment/100) * total_years))
        simple_interest_calculation_rounded = round(simple_interest_calculation, 2)
        print("\n")
        print(f"You will generate a total of {simple_interest_calculation_rounded} by simple interest.")

# compound interest calculation
    else:
        compound_interest_calculation = deposit * math.pow(1+(interest_rate_investment/100), total_years)
        compound_interest_calculation_rounded = round(compound_interest_calculation, 2)
        print("\n")
        print(f"You will generate a total of {compound_interest_calculation_rounded} by compound interest.")


# bond - inputs from user required
elif calculation_selection_lower == "bond":
    house_cost = float(input("Please enter the value of your house: "))
    interest_rate_bond = float(input("Please enter the interest rate: "))
    total_months = float(input("Please enter the total number of months you plan to repay the bond: "))

# bond calculations
    monthly_interest_rate = (interest_rate_bond/100) / 12
    bond_calculation = (monthly_interest_rate * house_cost) / (1 - (1 + monthly_interest_rate) ** (total_months *-1))
    bond_calculation_rounded = round(bond_calculation, 2)
    print("\n")
    print(f"You will have to pay {bond_calculation_rounded} monthly including interest.")


# invalid selections
else:
    print("Error. Please make a valid selection")


