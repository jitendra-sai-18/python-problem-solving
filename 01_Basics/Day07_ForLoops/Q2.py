# Q2. Print even numbers 1..N.
# Test cases:
# Input: 10
# Expected output: 2 4 6 8 10
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if i%2==0:
        print(i)



