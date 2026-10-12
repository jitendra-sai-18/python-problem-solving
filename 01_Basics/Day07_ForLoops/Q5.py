# Q5. Print multiplication table 1..10.
# Test cases:
# Input: 5
# Expected output: 5 10 15 20 25 30 35 40 45 50

n=int(input("Enter a number: "))
for i in range(1,11):
    j=n*i
    print(j)