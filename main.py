# Ask for inputs
income = round(float(input("Enter income: ")), 2)
expenses = round(float(input("Enter expenses: ")), 2)

# Calculate net income
net_income = round(income - expenses, 2)

# Print net income
print()
print("Net Income: $" + "{:.2f}".format(net_income))
print()

# Ask for inputs
current_savings = round(float(input("Enter current savings: ")), 2)
current_checking = round(float(input("Enter current checking: ")), 2)

# Calculate end of month savings and checking
savings_EOM = round(current_savings + net_income, 2)
checking_EOM = round(current_checking, 2)

# Calculate savings addition
savings_addition = round(savings_EOM - current_savings, 2)

# Calculate investment addition
investment_addition = round(net_income - savings_addition, 2)

# Calculate EOM finances
net_income = round(income - expenses, 2)
savings_EOM = round(current_savings, 2)
checking_EOM = round(current_checking, 2)
# savings_addition = round(savings_EOM - current_savings, 2)
# investment_addition = round(net_income - savings_addition, 2)

desired_checking_amount = 0  # Initializing desired_checking_amount to 0

print()

set_checking_desired = input("Do you want to set a desired amount for your checking account at the end of the month? (y/n): ")
print()

if set_checking_desired.lower() == "y":
  desired_checking_amount = round(float(input("Enter the desired amount for your checking account: ")), 2)
  print()

print("Desired Checking Amount: $" + "{:.2f}".format(desired_checking_amount))
print()

check_desired_correct = input("Is the desired checking amount correct? (y/n): ")
print()


# Calculate end of month savings and checking considering desired checking value
if checking_EOM < desired_checking_amount:
  checking_EOM = desired_checking_amount
  savings_to_checking_amount = desired_checking_amount - current_checking
  savings_EOM -= savings_to_checking_amount
  print("Moving $" + "{:.2f}".format(abs(savings_to_checking_amount)) + " from savings to checking")

elif checking_EOM > desired_checking_amount:
  excess_amount = checking_EOM - desired_checking_amount
  checking_EOM -= excess_amount
  savings_EOM += excess_amount
  print("Moving $" + "{:.2f}".format(abs(excess_amount)) + " from checking to savings")

else:
  print("Your books are balanced")

# Calculate investment amount
if net_income > 0 and savings_EOM > 2000:
  investment_potential = net_income * 0.8
  if savings_EOM - investment_potential <= 2000:
    investment_addition = (savings_EOM - 2000) * 0.8
    savings_EOM -= investment_addition
  elif savings_EOM - investment_potential > 2000:
    investment_addition = investment_potential
    savings_EOM -= investment_addition
  else:
    investment_addition = 0


# Print results
print()
print("Summary:")
print()
print("Money to invest: $" + "{:.2f}".format(investment_addition))
print("End of month Savings: $" + "{:.2f}".format(savings_EOM))
print("End of month Checking: $" + "{:.2f}".format(checking_EOM))
# print("Savings Addition: $" + "{:.2f}".format(savings_addition))
# print("Investment Addition: $" + "{:.2f}".format(investment_addition))