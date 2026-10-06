# Check triangle validity.
# Test cases:
# Input: 3 4 5
# Expected output: Valid
# Input: 1 2 3
# Expected output: Invalid

a=int(input("Enter a number a value: "))
b=int(input("Enter a number b value: "))
c=int(input("Enter a number c value: "))
if a+b> c and a+c> b and b+c> a:
    print("valid")
else:
    print("invalid")
