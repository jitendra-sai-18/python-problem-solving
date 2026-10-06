# Check leap year.
# Test cases:
# Input: 2024
# Expected output: Leap year
# Input: 1900
# Expected output: Not a leap year
# Input: 2000
# Expected output: Leap year

year=int(input("Enter a year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("it is a leap year")
else:
    print("it is NOT a leap year")
