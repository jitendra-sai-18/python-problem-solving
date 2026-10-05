# Calculate total cost from price and quantity.
# Test cases:
# Input: 120,3
# Expected output: 360
# Input: 49.5,2
# Expected output: 99.0

price=int(input("Enter the price of the product: "))
quantity=int(input("Enter the quantity of the product: "))
total=price*quantity
print(total)