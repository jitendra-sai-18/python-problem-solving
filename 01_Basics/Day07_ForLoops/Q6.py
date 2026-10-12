# Q6. Count numbers <=N divisible by both 3 and 5.
# Test cases:
# Input: 100
# Expected output: 6

n=int(input("Enter a number: "))
count=0
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        count=count+1
print(count)