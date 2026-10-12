# Q4. Find sum of odd numbers 1..N.
# Test cases:
# Input: 7
# Expected output: 16

n=int(input("Enter a number: "))
count=0
for i in range(1,n+1):
    if i%2!=0:
       count=i+count
print(count)