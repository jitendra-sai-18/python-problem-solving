# Q12. Palindrome number.
# Test cases:
# Input: 1221
# Expected output: Palindrome
# Input: 1234
# Expected output: Not palindrome
n=int(input("enter the number:"))
digits=len(str(n))
rev=0
for i in range(digits):
    value=n%10
    rev=rev*10+value
    remain_n=n//10
    n=remain_n
if rev==n:
    print("it is a palindrome")
else:
    print("it is not a palindrome")