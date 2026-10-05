# Calculate final price after percentage discount.
# Test cases:
# Input: 1000,10
# Expected output: 900.0
price=int(input("Enter price:"))
discount=int(input("Enter discount:"))
disprice=price*(discount/100)
final_price=price-disprice
print(final_price)