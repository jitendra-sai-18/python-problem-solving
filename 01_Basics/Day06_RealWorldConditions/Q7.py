# . Classify a valid triangle.
# Test cases:
# Input: 5 5 5
# Expected output: Equilateral
# Input: 5 5 3
# Expected output: Isosceles
# Input: 4 5 6
# Expected output: Scalene
s1=int(input("enter the side 1:"))
s2=int(input("enter the side 2:"))
s3=int(input("enter the side 3:"))
if s1==s2==s3:
    print("Equilateral triangle")
elif s1==s2 or s2==s3 or s1==s3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")