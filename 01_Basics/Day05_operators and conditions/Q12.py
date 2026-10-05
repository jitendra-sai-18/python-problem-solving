# Write a Python program that asks the user to enter:
# - The price of one notebook.
# - The number of notebooks purchased.
# Calculate and display:
# 1. The total cost.
# 2. The cost of one notebook multiplied by 3.
# 3. The amount remaining from ₹500 after paying the total cost.
# Use appropriate variable names and convert the inputs into numerical values.


p_n=float(input("enter the price of notebook:"))
n_b=int(input("enter the no of books purchased:"))
total_cost=p_n*n_b
threebooks=p_n*3
ra=500-total_cost
print("the total cost",total_cost)
print("the total cost of 3 books",threebooks)
print("the remaining amount",ra)
