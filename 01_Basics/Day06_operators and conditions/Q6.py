# Check divisibility by both 3 and 5.
# Test cases:
# Input: 30
# Expected output: Yes
# Input: 27
# Expected output: No
num=int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print("yes it is divisible by 3 & 5")
else:
    print("no it is not divisible by 3 & 5")