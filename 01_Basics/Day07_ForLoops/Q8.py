# Q8. Largest among N values.
# Test cases:
# Input: 5:4 18 7 3 12
# Expected output: 18

n=int(input("Enter a number: "))
num=list(map(int,input("Enter items: ").split()))

if n!=len(num):
    print("please enter numbers exactly")
else:
    value = num[0]
    for i in range(len(num)):
        if num[i] > value:
            value = num[i]
    print(value)
