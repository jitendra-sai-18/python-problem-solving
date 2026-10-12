# Q9. Count positive, negative and zero values.
# Test cases:
# Input: 6:2 -1 0 5 -4 0
# Expected output: Positive:2, Negative:2, Zero:2
num=(int(input("Enter a number: ")))
n=list(map(int,input("Enetr list of items:").split()))
if num!=len(n):
    print("please enter items exactly")
else:
    pov = 0
    nev = 0
    zero = 0
    for i in range(0, len(n)):
        if n[i] > 0:
            pov = pov + 1
        elif n[i] < 0:
            nev = nev + 1
        else:
            zero = zero + 1
    print("positive:", pov)
    print("negative:", nev)
    print("zeros:", zero)

