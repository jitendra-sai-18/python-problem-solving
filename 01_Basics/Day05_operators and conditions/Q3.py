# Classify a number as positive, negative or zero.
# Test cases:
# Input: -4
# Expected output: Negative
# Input: 0
# Expected output: Zero
num=int(input("Enter a number: "))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")