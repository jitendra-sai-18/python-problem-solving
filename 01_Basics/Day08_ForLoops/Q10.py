# Q10. Sum of digits.
# Test cases:
# Input: 472
# Expected output: 13
n=int(input("Enter a number: "))
digits=len(str(n))
value=0
for i in range(digits):
    value_n=n%10
    value=value_n+value
    value_n=n//10
    n=value_n
print(value)
