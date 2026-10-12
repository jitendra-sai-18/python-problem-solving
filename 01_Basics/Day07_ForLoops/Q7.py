# Q7. Factorial using a loop.
# Test cases:
# Input: 5
# Expected output: 120
# Input: 0
# Expected output: 1

n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact=i*fact
print(fact)