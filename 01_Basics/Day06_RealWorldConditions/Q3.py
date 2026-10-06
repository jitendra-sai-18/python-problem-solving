# Classify a character as uppercase, lowercase, digit or special.
# Test cases:
# Input: G
# Expected output: Uppercase
# Input: 7
# Expected output: Digit
# Input: @
# Expected output: Special
char=input("Enter value:")
if char.isupper():
    print("it is capital letter")
elif char.islower():
    print("it is lower case")
elif char.isdigit():
    print("it is digit")
else:
    print("it is special character")