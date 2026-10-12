# Q11. Reverse a number.
# Test cases:
# Input: 12340
# Expected output: 4321
n=int(input("enter the number:"))
digits=len(str(n))
rev=0
for i in range(digits):
    value=n%10
    rev=rev*10+value
    remain_n=n//10
    n=remain_n
print(rev)
