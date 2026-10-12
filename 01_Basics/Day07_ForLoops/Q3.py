# Q3. Find sum 1..N.
# Test cases:
# Input: 10
# Expected output: 55

n=int(input("Enter a number: "))
count=0
for i in range(1,n+1):
    count=i+count
print(count)